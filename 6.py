import hashlib
text = "fbyir".encode()
blake2b_hash = hashlib.blake2b(text).hexdigest()
print("BLAKE2b:", blake2b_hash)
