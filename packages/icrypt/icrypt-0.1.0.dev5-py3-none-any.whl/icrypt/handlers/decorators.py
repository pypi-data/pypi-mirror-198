
from functools import wraps

def pubkey_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # if not current_user.is_authenticated:
            # return redirect(url_for('auth.login'))

        # print(kwargs)
        return func(*args, **kwargs)
    return wrapper

def privkey_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # if not current_user.is_authenticated:
            # return redirect(url_for('auth.login'))

        # print(kwargs)
        return func(*args, **kwargs)
    return wrapper

# https://pgpy.readthedocs.io/en/latest/examples.html