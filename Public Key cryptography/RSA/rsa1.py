from advance_eculideab_algo import gcdExtended
from euclidea_algoithm import euclidean

p = 2
q = 7
n = p * q  # n is the moduls
euler_totient = (p - 1) * (q - 1)
e = 0  # encryption key
for i in range(1, euler_totient + 1):
    if euclidean(n, i) == 1:
        e = i

g, s, t = gcdExtended(e, euler_totient)
# decryption key
d = t
# choose another d from the same class of equivalence
for i in range(1, 12):
    if ((i * d) * e % euler_totient) == 1:
        d = i
encryption_pair = (d, n)  # public key
decryption_pair = (e, n)  # private key

# note: both private and public keys can be used interinterchangeably


def encryption(public_key, message):
    # try only one char
    position_in_alp = (ord(message) - 97) + 1
    e, n = public_key
    decrypted_message = pow(position_in_alp, e) % n
    decrypted_message = chr(decrypted_message + 96)
    return decrypted_message


cipher = encryption(encryption_pair, "b")
print(cipher)


def decryption(private_key, message):
    position_in_alp = (ord(message) - 97) + 1
    d, n = private_key
    decrypted_message = pow(position_in_alp, d) % n
    decrypted_message = chr(decrypted_message + 96)
    return decrypted_message


plain_text = decryption(decryption_pair, cipher)
print(plain_text)
