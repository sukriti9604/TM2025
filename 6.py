import hashlib
text = "Hello, World!".encode()
blake2b_hash = hashlib.blake2b(text).hexdigest()
print("BLAKE2b:", blake2b_hash)
