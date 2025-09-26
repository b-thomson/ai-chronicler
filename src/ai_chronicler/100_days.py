from string import ascii_lowercase
            
def encrypt(message: str, shift: int):
    
    encrypted_message = ""
    
    for char in message:
        shifted_char_idx = (ascii_lowercase.index(char) + shift) % len(ascii_lowercase)
        encrypted_message += ascii_lowercase[shifted_char_idx]
    
    return encrypted_message


def decrypt(message: str, shift: int):
    
    decrypted_message = ""
    
    for char in message:
        shifted_char_idx = (ascii_lowercase.index(char) - shift)
        decrypted_message += ascii_lowercase[shifted_char_idx]
    
    return decrypted_message

to_encrypt = "bawheed"
encrypted_message = encrypt(shift=2,message=to_encrypt)

#print(encrypted_message)

to_decrypt = "dcyjggf"
decrypted_message = decrypt(to_decrypt,2)

print(decrypted_message)
