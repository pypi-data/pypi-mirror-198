import os
import sys
import time
import json
import logdb
import hashlib


def append(client, blob):
    result = json.dumps(client.append(blob), indent=4, sort_keys=True)
    sys.stderr.write(result + '\n')


def tail(client, seq, step):
    chksum = ''
    for r in client.tail(seq, step):
        if 'blob' in r:
            blob = r.pop('blob', b'')
            if blob:
                x = hashlib.md5(blob).hexdigest()
                chksum += x
                y = hashlib.md5(chksum.encode()).hexdigest()
                res = 'log({}) blob({}) seq({}) len({})'.format(
                    y, x, r['seq'], len(blob))
                sys.stderr.write(res + '\n')
        else:
            time.sleep(1)


def put(client, key, blob):
    result = json.dumps(client.put(key, blob), indent=4, sort_keys=True)
    sys.stderr.write(result + '\n')


def get(client, key):
    result = client.get(key)
    blob = result.pop('blob', b'')
    sys.stderr.write(json.dumps(result, indent=4, sort_keys=True) + '\n\n')
    os.write(1, blob)


if '__main__' == __name__:
    client = logdb.Client(sys.argv[1].split(','))

    if 2 == len(sys.argv):
        append(client, sys.stdin.read())

    if 3 == len(sys.argv):
        if sys.argv[2].isdigit():
            tail(client, int(sys.argv[2]), 1)
        else:
            if os.path.basename(sys.argv[2]).isdigit():
                put(client, sys.argv[2], sys.stdin.read())
            else:
                get(client, sys.argv[2])

    if 4 == len(sys.argv):
        tail(client, int(sys.argv[2]), int(sys.argv[3]))
