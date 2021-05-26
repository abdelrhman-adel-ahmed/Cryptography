message = ""
# remove the spaces
message = "".join(message.split())


def encryptRailFence(text, key):

    # create rail matrix col = length of the message and row = len of the key
    rail = [["\n" for _ in range(len(text))] for _ in range(key)]
    # if we in first or last row that mean we will reverse the direction(go up or go down)
    # when we start the direction will be true because we in first row after that
    # we will do row+=1 untill enter the last row so the dictection will be false so we will enter row-=1
    direction = False
    row, col = 0, 0
    text_len = len(text)
    for i in range(text_len):
        if (row == 0) or (row == key - 1):
            direction = not direction
        # fill the current right index
        rail[row][col] = text[i]
        # we always incr the col
        col += 1
        # find the next row(go up or go down)
        if direction:
            row += 1
        else:
            row -= 1
    result = []
    for i in range(key):
        for j in range(text_len):
            if rail[i][j] != "\n":
                result.append(rail[i][j])
    return "".join(result)


def decrypt(cipher_text, key):

    """
    1-loop over and put dummy value in the each char right position in (zig zag way)
    2-supstite the dummy value with the corresponding char
    note:each row in wrote in Consecutive order
    3-read the rail in zig zag way and return the result
    """

    rail = [["\n" for _ in range(len(cipher_text))] for _ in range(key)]
    direction = False
    row, col = 0, 0
    text_len = len(cipher_text)
    for i in range(text_len):
        if (row == 0) or (row == key - 1):
            direction = not direction
        rail[row][col] = "*"
        col += 1
        if direction:
            row += 1
        else:
            row -= 1
    index = 0
    # now we replace the dummy with the coressponding char
    for i in range(key):
        for j in range(text_len):
            if rail[i][j] == "*":
                rail[i][j] = cipher_text[index]
                index += 1

    # read the rail in zig zag way
    result = []
    #beacuse the last direction above will be true (when we enter the last char 
    # [0][len(text)-1] position row == 0 and the direction is false from last time 
    # so it will be true)
    direction = False
    row, col = 0, 0
    for i in range(text_len):
        if (row == 0) or (row == key - 1):
            direction = not direction
        if rail[row][col] != "*":
            result.append(rail[row][col])
            col += 1

        # find the next row using
        # direction flag
        if direction:
            row += 1
        else:
            row -= 1
    return "".join(result)


cipher_text = encryptRailFence(message, 5)
print(cipher_text)
plain_text = decrypt(cipher_text, 5)
print(plain_text)
