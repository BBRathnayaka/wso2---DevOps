import hashlib
import sys
import os

hash_name = 'sha256'
rounds = 200000
salt = os.urandom(32)
password = sys.argv[1]

key = hashlib.pbkdf2_hmac(
    hash_name, # The hash digest algorithm for HMAC
    password.encode('utf-8'), # Convert the password to bytes
    salt, # Provide the salt
    rounds # It is recommended to use at least 100,000 iterations of SHA-256
)

print(key.hex())
