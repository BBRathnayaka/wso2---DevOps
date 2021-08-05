import hashlib
import sys
import os

salt = os.urandom(32)
input = sys.argv[1]
salted_input = str(salt) + input

hash = hashlib.sha512(salted_input.encode('utf-8')).hexdigest()
print(hash)
