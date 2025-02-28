import hashlib
text = "Hello world!".encode()
sha1_hash = hashlib.sha1(text).hexdigest()
print("SHA-1:", sha1_hash)

