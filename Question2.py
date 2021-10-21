#
# File        : Question2.py  
# Created     : 21/10/2021
# Author      : James Bowman
# Version     : v1.0.0
# Licensing   : (C) James Bowman
#               Available under GNU Public License (GPL)
# Description : 
#

from hashlib import blake2b
from hmac import compare_digest
import timeit

if __name__ == '__main__':

    SECRET_KEY = b'super secret hashing key'
    AUTH_SIZE = 16

    def sign(cookie):
        h = blake2b(digest_size=AUTH_SIZE, key=SECRET_KEY)
        h.update(cookie)
        return h.hexdigest().encode('utf-8')

    def password_encrypter():
        password = input("Please enter a password: ")
        starttime = timeit.default_timer()
        enc_password = sign(bytes(password, encoding='utf8'))
        print("Your encrypted password is {}".format(enc_password))
        print("Time to encrypt {}".format(timeit.default_timer() - starttime))
        return

    password_encrypter()
