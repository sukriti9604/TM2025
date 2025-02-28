import hashlib
text = "Hello world!".encode()
shake256_hash = hashlib.shake_256(text).hexdigest(32) 
print("SHAKE-256 (32 bytes):", shake256_hash)
