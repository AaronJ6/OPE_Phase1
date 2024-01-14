from pyope.ope import OPE
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import os
import json
import base64
from Crypto.Random import get_random_bytes

def generate_ope_key():
    return OPE.generate_key()

def generate_aes_key():
    return get_random_bytes(16)

def save_keys_to_json(ope_key, aes_key):
    with open('key.json', 'w') as f:
        json.dump({'OPE': ope_key.decode('latin-1'), 'AES': aes_key.decode('latin-1')}, f, indent=4)

def load_keys_from_json():
    with open('key.json', 'r') as f:
        keys = json.load(f)
        return keys['OPE'].encode('latin-1'), keys['AES'].encode('latin-1')
if not os.path.exists('key.json'):
    ope_key = generate_ope_key()
    aes_key = generate_aes_key()
    save_keys_to_json(ope_key, aes_key)
else:
    ope_key, aes_key = load_keys_from_json()
def ope_encrypt(data,key=ope_key):
    cipher = OPE(key)
    return cipher.encrypt(data)

def ope_decrypt(data,key=ope_key):
    cipher = OPE(key)
    try:
        return cipher.decrypt(data)
    except Exception as e:
        print("parts of the result obtained need not be decrypted")
        return data

def string_encrypt(message, key=aes_key):
    cipher = AES.new(key, AES.MODE_ECB)
    ciphertext = cipher.encrypt(pad(message.encode('utf-8'), AES.block_size))
    encoded_ciphertext = base64.b64encode(ciphertext).decode('utf-8')
    return encoded_ciphertext

def string_decrypt(encoded_ciphertext, key=aes_key):
    ciphertext = base64.b64decode(encoded_ciphertext)
    cipher = AES.new(key, AES.MODE_ECB)
    decrypted_message = unpad(cipher.decrypt(ciphertext), AES.block_size)
    return decrypted_message.decode('utf-8')



if __name__ == "__main__":
    print(ope_encrypt(123, ope_key))
    print(ope_decrypt(ope_encrypt(123, ope_key), ope_key))
    print(string_decrypt(string_encrypt('hello', aes_key)))
