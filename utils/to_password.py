import hashlib

def to_password(password):
    new_password = hashlib.md5(f"刘勇{password}测试".encode("utf-8")).hexdigest()
    return new_password
    