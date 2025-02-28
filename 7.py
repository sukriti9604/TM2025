import hashlib
text = "Hello world!".encode()
blake2s_hash = hashlib.blake2s(text).hexdigest()
print("BLAKE2s:", blake2s_hash)
