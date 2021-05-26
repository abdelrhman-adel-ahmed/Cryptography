import math

#traditional rail_fence with key fixed to 2 

plain_text = "welcome to my session"
# remove spaces
plain_text = "".join(plain_text.split())


def encrypt(message):
    cipher_text = ""
    message_len = len(message)
    for i in range(0, message_len, 2):
        cipher_text += message[i]
    for i in range(1, message_len, 2):
        cipher_text += message[i]
    return cipher_text


"""
(draw line put chars in upper part of the line and lower part interchangeably)
if len of the cipher_text is even then the two part the upper and lower will be even 
if len of the cipher_text is odd then len of the first part will be higher by 1  
"""


def decrypt(cipher_text):
    message_len = len(cipher_text)
    first_part_len = math.ceil(message_len / 2)
    second_part_len = message_len - first_part_len
    first_part = cipher_text[0:first_part_len]
    second_part = cipher_text[first_part_len:message_len]
    plain_text = ""
    for i, j in zip(first_part, second_part):
        plain_text += i
        plain_text += j
    # zip function take eqaul parts
    if message_len % 2 != 0:
        plain_text += first_part[len(first_part) - 1]
    return plain_text


enc = encrypt(plain_text)
dec = decrypt(enc)
print(enc)
print(dec)
