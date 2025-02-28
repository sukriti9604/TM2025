import hashlib
text = "ner".encode()
sha1_hash = hashlib.sha1(text).hexdigest()
print("SHA-1:", sha1_hash)

