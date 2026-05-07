from cryptography.fernet import Fernet
import os
import json
import base64
file_name = 'key.json'
if os.path.exists(file_name):
       with open(file_name) as x:
              all_data = json.load(x)
else:
       all_data = []
key = Fernet.generate_key()
f = Fernet(key)
cardNumber = 1234123412341234
token = f.encrypt(str(cardNumber).encode())
token
# b'...'
# f.decrypt(token)
print('Key:', key.decode('utf-8'))
print('Encrypted Number', token)
all_data.append({
        'key':base64.b64encode(key).decode('utf-8'),
        'token':base64.b64encode(token).decode('utf-8')
})
with open(file_name,'w') as x:
                json.dump(all_data,x,indent=2)
print(f'Key Saved!')
decrypted = f.decrypt(token).decode('utf-8')
print('Decrypted Number', decrypted)
# print(Ecrypyed)

