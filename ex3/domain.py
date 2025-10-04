import unicodedata
import string

SYMBOLS = set(string.punctuation)

def _normalize(s: str) -> str:
    nfkd = unicodedata.normalize("NFKD", s)
    return ''.join(ch for ch in nfkd if not unicodedata.combining(ch)).lower()

def is_strong_password(pwd: str, username: str) -> bool:
    if not isinstance(pwd, str) or not isinstance(username, str):
        return False

    if pwd != pwd.strip():
        return False

    if len(pwd) < 10:
        return False

    has_upper = any(c.isupper() for c in pwd)
    has_lower = any(c.islower() for c in pwd)
    has_digit = any(c.isdigit() for c in pwd)
    has_symbol = any(c in SYMBOLS for c in pwd)

    if not (has_upper and has_lower and has_digit and has_symbol):
        return False

    for i in range(len(pwd) - 2):
        if pwd[i] == pwd[i+1] == pwd[i+2]:
            return False

    norm_pwd = _normalize(pwd)
    norm_user = _normalize(username)

    if norm_user in norm_pwd:
        return False

    return True
