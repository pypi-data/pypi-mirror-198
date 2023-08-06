from pgpy.constants import PubKeyAlgorithm, KeyFlags, HashAlgorithm, \
                            SymmetricKeyAlgorithm, CompressionAlgorithm
from pgpy import PGPKey, PGPUID, PGPMessage
from .decorators import pubkey_required, privkey_required


class PGPHandler:

    @staticmethod
    def generate_key(name, email, path=None):
        key = PGPKey.new(PubKeyAlgorithm.RSAEncryptOrSign, 4096)
        uid = PGPUID.new(name, email=email)
        key.add_uid(uid, 
                        usage={
                            KeyFlags.Sign, 
                            KeyFlags.EncryptCommunications,
                            KeyFlags.EncryptStorage
                        },
                    hashes=[
                            HashAlgorithm.SHA256,
                            HashAlgorithm.SHA384,
                            HashAlgorithm.SHA512,
                            HashAlgorithm.SHA224
                            ],
                    ciphers=[
                            SymmetricKeyAlgorithm.AES256,
                            SymmetricKeyAlgorithm.AES192,
                            SymmetricKeyAlgorithm.AES128,
                            # SymmetricKeyAlgorithm.CAST5,
                            ],
                    compression=[
                            CompressionAlgorithm.ZLIB,
                            CompressionAlgorithm.BZ2,
                            CompressionAlgorithm.ZIP,
                            CompressionAlgorithm.Uncompressed
                            ])
        return key
    
    @staticmethod
    @pubkey_required
    def encrypt(**kwargs):
        pubkey = kwargs["pubkey"]
        message = PGPMessage.new(kwargs["message"])
        encrypted = pubkey.encrypt(message)
        return encrypted

    @staticmethod
    @privkey_required
    def decrypt(**kwargs):
        privkey = kwargs["privkey"]
        encrypted = kwargs["encrypted"]
        decrypted = privkey.decrypt(encrypted).message
        return decrypted


# python -m icrypto.handlers.pgp_handler
if __name__ == "__main__":
    pgp_handler = PGPHandler()
    key = pgp_handler.generate_key(name="Test", email="asdf@asdf.com")
    print(key.pubkey)
    pubkey = PGPKey.from_file('pubkey.txt')
    # a = pgp_handler.encrypt(pubkey=pubkey, message='asdf')





