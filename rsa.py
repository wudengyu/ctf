from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5
from Crypto.Util import number
import base64
p=273821108020968288372911424519201044333
q=280385007186315115828483000867559983517
n=76775333340223961139427050707840417811156978085146970312315886671546666259161
e=65537
d=number.inverse(e,(p-1)*(q-1))
#cryptotext='Ni45iH4UnXSttNuf0Oy80+G5J7tm8sBJuDNN7qfTIdEKJow4siF2cpSbP/qIWDjSi+w='
cryptotext=b'\x8D\xDB\xF1\x0E\xB8\x14\xBB\xE6\x0C\xB0\x59\x57\xA2\x44\x5A\xE9\x9F\x11\xA1\xE6\xEE\x33\x87\x70\x82\xD8\xD2\xB0\x14\x28\xD7\x31'
private_key=RSA.construct([n,e,d])
cipher_rsa = PKCS1_v1_5.new(private_key)
sentinel = None
#data=cipher_rsa.decrypt(base64.b64decode(cryptotext),sentinel).decode('utf-8')
data=cipher_rsa.decrypt(cryptotext,sentinel).decode('utf-8')
print(data)
