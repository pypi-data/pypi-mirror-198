from .pgp_handler import PGPHandler
from pgpy import PGPKey, PGPUID, PGPMessage


class ICrypt:

    @staticmethod
    def generate_key(**kwargs):
        # key = self.pgp_handler.generate_key(**kwargs)
        key = PGPHandler.generate_key(**kwargs)
        return key

    @staticmethod
    def encrypt(pubkey_path, message):
        pubkey, _ = PGPKey.from_file(pubkey_path)
        return PGPHandler.encrypt(pubkey=pubkey, message=message)
    
    @staticmethod
    def decrypt(privkey_path, encrypted_file_path):
        privkey, _ = PGPKey.from_file(privkey_path)
        encrypted = PGPMessage.from_file(encrypted_file_path)
        return PGPHandler.decrypt(privkey=privkey, encrypted=encrypted)


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