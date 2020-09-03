from base64 import *
import codecs

flag = 'flag'
cipher='0URT4NPdOOPZbNQbWtQdMtRhMNnTDuOdMtNfMtPzWtnPfUpxcao'

def encrypt(str):
    s = ''
    for i in range(len(str)):
        if str[i] != '{' and str[i] != '}':
            s += chr((ord(str[i])-47)<<1)
        else:
            s += chr(ord(str[i]))
    s1 = b64encode(s.encode('utf-8'))
    s2 = s1[::-1]
    print('s1:',s1)
    s3 = codecs.encode(s2.decode('utf-8'), "rot13" )
    return s3
def decrypt(str):
    s3=b64decode(codecs.decode(str,"rot13").encode('utf-8')[::-1]+b'=')
    s=''
    for i in range(len(s3)):
        if chr(s3[i])!='{' and chr(s3[i])!='}':
            s+=chr((s3[i]>>1)+47)
        else:
            s+=chr(s3[i])
    return s
#cipher = encrypt(flag)
flag=decrypt(cipher)
print(flag)
#cipher：=0URT4NPdOOPZbNQbWtQdMtRhMNnTDuOdMtNfMtPzWtnPfUpxcao
