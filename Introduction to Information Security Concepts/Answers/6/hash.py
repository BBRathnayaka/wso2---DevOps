import hashlib
import sys

hash_name = 'sha256'
rounds = 200000
salt = 'Km5d5ivMy8iexuHcZrsD'
password = sys.argv[1]

key = hashlib.pbkdf2_hmac(
    hash_name, # The hash digest algorithm for HMAC
    password.encode('utf-8'), # Convert the password to bytes
    salt.encode('utf-8'), # Provide the salt
    rounds # It is recommended to use at least 100,000 iterations of SHA-256
)

print(key.hex())
