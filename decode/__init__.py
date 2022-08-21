import argparse
import base64
import hashlib
import json
import os
from rich import print
from Crypto.Cipher import AES


def start_parser() -> argparse.Namespace:  # start parser for command line arguments and start download process
    parser = argparse.ArgumentParser()  # create parser object for command line arguments
    parser.add_argument("-r", "--read", default=False, action="store_true", help="read local file")
    parser.add_argument("-d", "--data", nargs=1, default=None, help="input data")

    return parser.parse_args()


def decrypt(encrypted: str, key='zG2nSeEfSHfvTCHy5LCcqtBbQehKNLXn') -> [int, bytes]:
    decrypt_data = AES.new(hashlib.sha256(key.encode('utf-8')).digest(), AES.MODE_CBC, b'\0' * 16). \
        decrypt(base64.b64decode(encrypted))
    return decrypt_data[0:len(decrypt_data) - ord(chr(decrypt_data[len(decrypt_data) - 1]))]


def main():
    try:
        args = start_parser()
        if args.read:
            if os.path.exists("hbooker.txt"):
                result = open("hbooker.txt", 'r', encoding='utf-8').read()
                print(json.loads(decrypt(result).decode('utf-8')))
            else:
                open('hbooker.txt', 'w', encoding='utf-8')
                print("[error] hbooker.txt not found, start to create it")
        elif args.data is not None:
            print(json.loads(decrypt(args.data[0]).decode('utf-8')))
    except Exception as e:
        print("error:", e)
