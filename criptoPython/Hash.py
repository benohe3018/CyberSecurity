import hashlib

#Stablish the method of encryption
message_in_sha224 = hashlib.sha224()
message_in_sha224.update(bytes("hello everybody","utf8"))
print("Message in sha 224 is: ", message_in_sha224.digest().hex())
print("The hash size is: ", message_in_sha224.digest_size)

#Stablish the method of encryption
message_in_sha256 = hashlib.sha256()
#Write a meesage and Update it
message_in_sha256.update(bytes("hello everybody","utf8"))
#Print the message
print("Message in sha256:", message_in_sha256.digest().hex())
print("The hash size is: ", message_in_sha256.digest_size, " bytes")

#Stablish teh method of encryption
message_in_sha384 = hashlib.sha384()
#Write a message and update it
message_in_sha384.update(bytes("hello everybody","utf8"))
#Print the message
print("Message in sha 384 is: ", message_in_sha384.digest().hex())
print("The hash size is: ", message_in_sha384.digest_size, " bytes")

#Stablish the encryption method
message_in_md5 = hashlib.md5()
#Write a message and update it
message_in_md5.update(bytes("hello everybody", "utf8"))
#Print the message
print("Message in md5 is: ", message_in_md5.digest().hex())
print("Tha hash size is: ", message_in_md5.digest_size, " bytes")

#Stablish the method of encryption
message_in_sha1 = hashlib.sha1()
#Write a message and Update it
message_in_sha1.update(bytes("hello everyboy","utf8"))
#Print the message
print("Message in sha1 = ", message_in_sha1.digest().hex())
print("The hash size is: ", message_in_sha1.digest_size, " bytes")

#Stablish the method of encryption
message_in_sha3_512 = hashlib.sha3_512()
#Write a message and update it
message_in_sha3_512.update(bytes("hello everybody","utf8"))
#Print the message
print("Message in sha3_512 is: ", message_in_sha3_512.digest().hex())
print("the hash size is: ", message_in_sha3_512.digest_size, " bytes")

