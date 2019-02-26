import nacl.secret
import nacl.utils

def bitstring_to_bytes(s):
    v = int(s, 2)
    b = bytearray()
    while v:
        b.append(v & 0xff)
        v >>= 8
    return bytes(b[::-1])


print(bin(999))
key0 = '1111100111'
subkey0 = '11100111'
subkey1 = '11000000'
subkey0_byte = bitstring_to_bytes(subkey0)
subkey1_byte = bitstring_to_bytes(subkey1)
zero_byte = b'\x00'
subkey = subkey0_byte + subkey1_byte
for x in range(1,31):
  subkey = subkey + zero_byte 

# This is your safe, you can use it to encrypt or decrypt messages
box = nacl.secret.SecretBox(key)

infile = "L12-14.enc.pdf"

with open(infile, "rb") as in_file:
    data = in_file.read()
    
# Decrypt our message, an exception will be raised if the encryption was
#   tampered with or there was otherwise an error.
decrypted = box.decrypt(data)

outfile = "decrypt.pdf"

with open("outfile", "wb") as out_file:
    out_file.write(decrypted)

