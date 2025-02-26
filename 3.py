import hashlib
text = "Hello, World!".encode()
sha256_hash = hashlib.sha256(text).hexdigest()
print("SHA-256:", sha256_hash)