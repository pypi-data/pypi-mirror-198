import os
import random
import requests

requests.packages.urllib3.disable_warnings()


class Client:
    def __init__(self, servers):
        self.servers = servers
        self.session = requests.Session()
        self.url_type = 'http'

        TLS_FILES = ['ca.pem', 'client.pem', 'client.key']
        if any([os.path.isfile(f) for f in TLS_FILES]):
            self.url_type = 'https'
            self.session.cert = ('client.pem', 'client.key')
            self.session.verify = 'ca.pem'

    def tail(self, seq, step=1):
        while True:
            srv = '{}://{}'.format(self.url_type, random.choice(self.servers))
            res = dict(server=srv, seq=seq)
            try:
                r = self.session.get('{}/{}'.format(srv, seq))
                if 200 != r.status_code:
                    raise Exception('http_response : {}'.format(r.status_code))

                res.update(dict(blob=r.content))
                yield res

                seq += step
            except Exception as e:
                res.update(dict(exception=str(e)))
                yield res

    def append(self, blob):
        for i in range(len(self.servers)):
            srv = '{}://{}'.format(self.url_type, random.choice(self.servers))

            try:
                r = self.session.post(srv, data=blob)
                if 200 == r.status_code:
                    return dict(srv=srv, seq=r.headers['x-seq'])
            except Exception:
                pass

    def put(self, key, blob):
        for i in range(len(self.servers)):
            srv = '{}://{}'.format(self.url_type, random.choice(self.servers))
            key = key.strip('/')

            try:
                r = self.session.put('{}//{}'.format(srv, key), data=blob)
                if 200 == r.status_code:
                    return dict(srv=srv, status=r.headers['x-status'])
            except Exception:
                pass

    def get(self, key):
        for i in range(len(self.servers)):
            srv = '{}://{}'.format(self.url_type, random.choice(self.servers))
            key = key.strip('/')

            try:
                r = self.session.get('{}//{}'.format(srv, key))
                if 200 == r.status_code:
                    return dict(srv=srv, blob=r.content,
                                seq=int(r.headers['x-seq']))
            except Exception:
                pass
