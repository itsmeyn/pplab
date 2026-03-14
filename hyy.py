plain_text = input("Enter plain text: ")
key = int(input("Enter key value: "))

cipher_text = ""

for i in plain_text:
    ordvalue = ord(i)
    ciphervalue = ordvalue + key
    cipher_text += chr(ciphervalue)

print(cipher_text)
                         
