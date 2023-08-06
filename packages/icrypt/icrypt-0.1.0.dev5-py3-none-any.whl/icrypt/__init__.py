# from icrypto.icrypto_old import icrypto as crypto

# encrypt = crypto.encrypt
# decrypt = crypto.decrypt

from icrypt.icrypt import ICrypt as crypto

generate_key = crypto.generate_key
encrypt = crypto.encrypt
decrypt = crypto.decrypt

import handlers

__all__ = [
    "handlers",
    "crypto",
]