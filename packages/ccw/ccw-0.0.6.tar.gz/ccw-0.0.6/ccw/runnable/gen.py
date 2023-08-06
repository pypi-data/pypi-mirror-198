# standard imports
import os
import secrets
import sys
import json
import hashlib

ELEVEN_BITS = 0x00000000000000000000000000000000000000000000000000000000000007ff

script_dir = os.path.realpath(os.path.dirname(__file__))
data_dir = os.path.join(script_dir, '..', 'data')

def main():
    wordlist_filepath = os.path.join(data_dir, 'english.json')
    f = open(wordlist_filepath, 'r')
    ls = json.load(f)
    f.close()

    entropy = os.urandom(32)
    h = hashlib.sha256()
    h.update(entropy)
    z = h.digest()
    seed_bytes = entropy + z[0:1] # checksum is up to bit boundary divisible by 11
    seed = int.from_bytes(seed_bytes, byteorder='big')

    r = []
    for i in range(24):
        r.append(int((seed >> ((23 - i) * 11)) & ELEVEN_BITS))

    have = False
    for v in r:
        if have:
           sys.stdout.write(' ') 
        sys.stdout.write(ls[v])
        have = True


if __name__ == '__main__':
    main()
