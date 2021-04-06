
#https://en.wikipedia.org/wiki/Polybius_square

def polybiusCipherEncrypt(s):
    encrypt = ""
    # convert each character to its encrypted code
    for char in s:

        # finding row of the table
        row = int((ord(char) - ord("a")) / 5) + 1

        # finding column of the table
        col = ((ord(char) - ord("a")) % 5) + 1

        # if character is 'k'
        if char == "k":
            row = row - 1
            col = 5 - col + 1

        # if character is greater than 'j'
        elif ord(char) >= ord("j"):
            if col == 1:
                col = 6
                row = row - 1
            col = col - 1

        r = str(row)
        c = str(col)
        encrypt += r + c
    return encrypt


def polybiusCipherDecrypt(num):
    li = list(num)
    dec = ""
    for i in range(0, len(li) - 1, 2):
        r = int(li[i])
        c = int(li[i + 1])
        ch = chr((r - 1) * 5 + c + 96)
        if ord(ch) - 96 >= 10:
            ch = chr((r - 1) * 5 + c + 96 + 1)
        ch1 = str(ch)
        dec += ch1
    return dec


e = polybiusCipherEncrypt("hi")
d = polybiusCipherDecrypt(e)
print(d)
