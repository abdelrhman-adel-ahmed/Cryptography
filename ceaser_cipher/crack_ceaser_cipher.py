"""
"""

encrypted_message=""


def convert_text(x):
    """
    convert letters in text into the coresspoding alphabetic order
    """
    l = list()
    x = x.lower()
    for i in x:
        num = ord(i) - ord("a") + 1
        l.append(num)
    return l


def cal_occurence(correspoding_text_number_list):
    """
    calcualte each occurence of a number in a list
    """
    di = dict()
    for i in correspoding_text_number_list:
        i = str(i)
        s = di.get(i, 0)
        if s == 0:
            di[i] = 1
        else:
            di[i] = di[i] + 1
    return di


def get_heighest_val_in_dic(di):
    num = 0
    val = 0
    for i in di.keys():
        if di[i] > num:
            num = di[i]
            val = i
    hi = (val, num)
    return hi


def get_heighest_val_char(t, correspoding_text_number_list):
    """
    get the heighest value corresponding letter
    1-get the position of the number in the list (we get the number from the tuple)
    2-then find the corresponding letter index in the text
    """
    positon_in_the_list = correspoding_text_number_list.index(int(t[0]))
    char = x[positon_in_the_list]
    return char


def get_the_key(t):
    """
    get the key by calculte how many number it shift from letter e possiton
    """
    number = int(t[0])
    key = number - 5
    return key


def crack_cipher(x):
    correspoding_text_number_list = convert_text(x)
    d = cal_occurence(correspoding_text_number_list)
    hi = get_heighest_val_in_dic(d)
    val = get_heighest_val_char(hi, correspoding_text_number_list)
    key = get_the_key(hi)
    return key


print(crack_cipher(encrypted_message))
