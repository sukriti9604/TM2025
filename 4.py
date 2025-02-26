import hashlib
text = "Hello, World!".encode()
sha512_hash = hashlib.sha512(text).hexdigest()
print("SHA-512:", sha512_hash)