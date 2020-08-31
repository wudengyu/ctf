import itertools as its
import hashlib
words='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
#words='0123456789'
r=its.product(words,repeat=4)
for trying in r:
    trying=trying+('L','i','H','u','a')
    md5=hashlib.md5("".join(trying).encode("utf-8")).hexdigest()
    if md5[0:16]=='1a4fb3fb5ee12307':
        print(trying)
        print(md5)
        break