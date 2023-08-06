#!/usr/bin/python3

# standard imports
import os
import sys
import logging
import argparse
import json

# third-party imports
from bip_utils import Bip39SeedGenerator, Bip32Secp256k1 as Bip32, Bip44Changes

logging.basicConfig()
logg = logging.getLogger()


argparser = argparse.ArgumentParser()
argparser.add_argument('-v', action='store_true', help='verbose logging')
argparser.add_argument('-n', type=int, default=10, help='number of addresses to derive')
argparser.add_argument('-p', action='store_true', default=False, help='include private keys in output')
argparser.add_argument('--bip', type=int, default=44, choices=[44, 49, 84], help='BIP derivation curve')
argparser.add_argument('mnemonic', type=str, nargs='?', help='mnemonic')
args = argparser.parse_args()

if args.v:
    logg.setLevel(logging.DEBUG)

mnemonic = args.mnemonic
if mnemonic == None:
    mnemonic = os.environ.get('MNEMONIC')
if mnemonic == None:
    raise AttributeError('Mnemonic must be provided either as positional argument or environment variable MNEMONIC')
    sys.exit(1)

seed = Bip39SeedGenerator(mnemonic)
seed_bytes = seed.Generate()
logg.debug('seed {}'.format(seed_bytes))

b = seed_bytes
#b = Bip32.FromSeedAndPath(seed_bytes, "m/44'/60'/0'/2")
if args.bip == 44:
    from bip_utils import Bip44, Bip44Coins
    b = Bip44.FromSeed(b, Bip44Coins.BITCOIN)
elif args.bip == 49: 
    from bip_utils import Bip49, Bip49Coins
    b = Bip49.FromSeed(b, Bip49Coins.BITCOIN)
elif args.bip == 84:
    from bip_utils import Bip84, Bip84Coins
    b = Bip84.FromSeed(b, Bip84Coins.BITCOIN)
else:
    raise ValueError('Invalid BIP value: {}'.format(args.bip))

keys = {
        'public': [],
        'address': [],
    }
if args.p:
    keys['private'] = []


def main():
    for i in range(args.n):
        be = b.Purpose().Coin().Account(0)
        be = be.Change(Bip44Changes.CHAIN_EXT)
        be = be.AddressIndex(i)
        #be = Bip32.FromSeedAndPath(seed_bytes, "m/44'/60'/0'/2/" + str(i))
        pk = be.PrivateKey()
        pubk = be.PublicKey()

        pk_hex = pk.Raw().ToBytes().hex()
        logg.debug('pk {}'.format(pk_hex))

        pubk_hex = pubk.RawCompressed().ToBytes().hex()
        logg.debug('pubk {}'.format(pubk_hex))

        eth_address = pubk.ToAddress()
        logg.debug('addr {}'.format(eth_address))

        if args.p:
            keys['private'].append('0x' + pk_hex)
        keys['public'].append('0x' + pubk_hex)
        keys['address'].append(eth_address)

    sys.stdout.write(json.dumps(keys))


if __name__ == '__main__':
    main()
