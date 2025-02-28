import hashlib
text = "Hello world!".encode()
shake128_hash = hashlib.shake_128(text).hexdigest(16)  
print("SHAKE-128 (16 bytes):", shake128_hash)
