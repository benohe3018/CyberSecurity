package main

import (
	"crypto/aes"
	"crypto/cipher"
	"crypto/rand"
	"encoding/hex"
	"fmt"
	"io"
)

func main() {
	//We start with the message tpo encrypt
	message := []byte("Today its a great day to start encrypting some message under Golang Languaje")

	//We declare our hexadecimal key
	key, _ := hex.DecodeString("c936108299307d3f6f7585b96013346d")

	//We declare our nonce and put in it a try catch sentence to catch any errors
	nonce := make([]byte, 12)
	if _, err := io.ReadFull(rand.Reader, nonce); err != nil {
		panic(err.Error)
	}

	// We start our encrypt in AES algorithm with GCM mode
	block, err := aes.NewCipher(key)
	if err != nil {
		panic(err.Error())
	}

	aesgcm, err := cipher.NewGCM(block)
	if err != nil {
		panic(err.Error())
	}

	// Encrypt and authenticate
	ciphertext := aesgcm.Seal(nil, nonce, message, nil)

	// Show the encrypted and MAC id!!!
	fmt.Printf("Cipher_text is: %x\n", ciphertext[:len(ciphertext)-aesgcm.Overhead()])
	fmt.Printf("Tag is: %x\n", ciphertext[len(ciphertext)-aesgcm.Overhead():])
}
