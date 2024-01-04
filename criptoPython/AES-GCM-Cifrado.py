from Crypto.Cipher import AES

#Let´s declare a message to encrypt
message = bytes('Toda its a great day to start encryptying some maessage under an AES cipher and GCM mode', 'utf8')

#Declare our key in hex
key = bytes.fromhex('c936108299307d3f6f7585b96013346d')
#Declare our nonce in hex
nonce = bytes.fromhex('47e6831df094b7a6')

#Declare our associate data
associate_data = bytes('Today is tursday','utf8')

#Lets go and cipher
cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
#Update the cipher usin our associate datta
cipher.update(associate_data)
#Cipher and authenticate
cipher_text, mac = cipher.encrypt_and_digest(message)

#Pu it on the screen
print("Cipher_text is: ", cipher_text.hex())
print("Tag is: ", mac.hex())