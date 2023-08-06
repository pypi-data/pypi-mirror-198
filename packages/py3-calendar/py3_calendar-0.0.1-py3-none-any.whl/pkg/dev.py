import secrets as sec


key = sec.token_hex(nbytes=10)
key_bytes = sec.token_bytes(16)
key_urlsafe = sec.token_urlsafe(10)

print(key)
print(key_bytes)
print(key_urlsafe)