import hashlib
text = "Hello world!".encode()
sha256_hash = hashlib.sha256(text).hexdigest()
print("SHA-256:", sha256_hash)