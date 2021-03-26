def cipher_encryption(word, key):
    encrypted_message = ""
    for i in word:
        letter = ord(i) - ord("a") + 1
        encrypted_letter = (letter + key) % 26
        s = chr(encrypted_letter + 97 - 1)
        encrypted_message += s
    return encrypted_message


def cipher_decrypte(word, key):
    decrypted_message = ""
    for i in word:
        letter = ord(i) - ord("a") + 1
        decrypted_letter = (letter - key) % 26
        decrypted_letter = chr(decrypted_letter + 97 - 1)
        decrypted_message += decrypted_letter
    return decrypted_message
