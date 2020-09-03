from base64 import *
import codecs
cipher='cnh1c28gICIlISIkLScjInAnISYlJiByLS0sJCx1dyYgI3UnJWk='
s=b64decode(cipher)
flag=''
for i in range(len(s)):
    flag+=chr(s[i]^20)
print(flag)
