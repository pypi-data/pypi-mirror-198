from handlers.pgp_handler import PGPHandler
from pgpy import PGPKey, PGPUID, PGPMessage
import os


class ICrypt:

    def __init__(self):
        self.pgp_handler = PGPHandler()

    def generate_key(self, **kwargs):
        key = self.pgp_handler.generate_key(**kwargs)
        return key

    def encrypt(self, pubkey_path, message):
        pubkey, _ = PGPKey.from_file(pubkey_path)
        return self.pgp_handler.encrypt(pubkey=pubkey, message=message)
        
    def decrypt(self, privkey_path, encrypted):
        privkey, _ = PGPKey.from_file(privkey_path)
        return self.pgp_handler.decrypt(privkey=privkey, encrypted=encrypted)


if __name__ == '__main__':
    ic = ICrypt()
    # key = ic.generate_key(name="Test", email="test.com")
    # print(key.pubkey)
    # print(key)
  
    en_msg = ic.encrypt(pubkey_path="sample_pubkey.txt", message="Hello World")
    print(en_msg)

    f = open("sample_encrypted.txt", "w")
    f.write(str(en_msg))
    f.close()

    encrypted= PGPMessage.from_file("sample_encrypted.txt")
    # print(encrypted)
    msg = ic.decrypt(privkey_path="sample_privkey.txt", encrypted=encrypted)
    print(msg)

    # msg = ic.decrypt(privkey_path="privkey.txt", encrypted=en_msg)
    # print(msg)