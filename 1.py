import hashlib
text = "Hello world!".encode()
md5_hash = hashlib.md5(text).hexdigest()
print("MD5:", md5_hash)