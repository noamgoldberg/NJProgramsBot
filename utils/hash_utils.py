import hashlib

def hash_str(s: str) -> str:
    return hashlib.sha256(s.encode()).hexdigest()
