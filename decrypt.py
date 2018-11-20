import nacl.secret
import nacl.utils
import base64

# This must be kept secret, this is the combination to your safe
key = 'h8zxgs5SRG4tGa+Vs/2vWJ/NLlLySoicnJ4ysr3l3OQ='
key = base64.b64decode(key)

# This is your safe, you can use it to encrypt or decrypt messages
box = nacl.secret.SecretBox(key)

infile = "L08-11.enc.pdf"

with open(infile, "rb") as in_file:
    data = in_file.read()
    
# Decrypt our message, an exception will be raised if the encryption was
#   tampered with or there was otherwise an error.
decrypted = box.decrypt(data)

outfile = "decrypt.pdf"

with open("outfile", "wb") as out_file:
    out_file.write(decrypted)
