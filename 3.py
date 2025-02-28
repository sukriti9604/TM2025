import hashlib
text = "irel".encode()
sha256_hash = hashlib.sha256(text).hexdigest()
print("SHA-256:", sha256_hash)