def encrypt(word, key):
    count = 0
    key_length = len(key)
    decrypted_message = ""
    for i in word:
        if count > key_length - 1:
            count = 0
        # will not add one because we start from 0 to 25
        letter_num = ord(i) - ord("a")
        key_letter_num = ord(key[count]) - ord("a")
        decrypted_letter = (letter_num + key_letter_num) % 26
        decrypted_letter = chr(decrypted_letter + 97)
        decrypted_message += decrypted_letter
        count += 1
    return decrypted_message


def decrypt(word, key):
    count = 0
    key_length = len(key)
    decrypted_message = ""
    for i in word:
        if count > key_length - 1:
            count = 0
        letter_num = ord(i) - ord("a")
        key_letter_num = ord(key[count]) - ord("a")
        decrypted_letter = (letter_num - key_letter_num) % 26
        decrypted_letter = chr(decrypted_letter + 97)
        decrypted_message += decrypted_letter
        count += 1
    return decrypted_message
