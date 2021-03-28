
letterFrequency = {
    "E": 12.0,
    "T": 9.10,
    "A": 8.12,
    "O": 7.68,
    "I": 7.31,
    "N": 6.95,
    "S": 6.28,
    "R": 6.02,
    "H": 5.92,
    "D": 4.32,
    "L": 3.98,
    "U": 2.88,
    "C": 2.71,
    "M": 2.61,
    "F": 2.30,
    "Y": 2.11,
    "W": 2.09,
    "G": 2.03,
    "P": 1.82,
    "B": 1.49,
    "V": 1.11,
    "K": 0.69,
    "X": 0.17,
    "Q": 0.11,
    "J": 0.10,
    "Z": 0.07,
}


def get_concidences_list(message):
    """
    crate shifted messages from each message and in each shited message compare the positions of the
    letters to the original cipher and if it match increament the concidences by 1
    e.x message-> iloveyou
                   iloveyo
                    ilovey
                    ...
    so in the first shifted message we comapre (l,i) (o,l) (v,o) (e,v) .... in if letter in the original message
    match with letter in the shifted text we increament the concidence by 1
    """
    concidences = list()
    for i in range(1, len(message)):
        li = message[0 : len(message) - i]
        print(li)
        concidences.insert(i - 1, 0)
        for j in range(i, len(message)):
            if li[j - i] == message[j]:
                concidences[i - 1] += 1
    return concidences


concidences_list = get_concidences_list(message)
print(concidences_list)


def get_the_highest_concidences(concidences):
    sorted_concidences = concidences.copy()
    sorted_concidences.sort(reverse=True)
    print(sorted_concidences)
    return sorted_concidences


def get_the_key_length(sorted_concidences, concidences_list):
    max_peak = sorted_concidences[0]
    key_length = 0
    find_highest = False
    for i in concidences_list:
        if i == max_peak and key_length == 0:
            key_length += 1
            find_highest = True
        elif i == max_peak:
            break
        elif find_highest:
            key_length += 1
    return key_length


def slice_the_cipher_text(message, key_length):
    list_of_splited_litters = [message[i : i + key_length] for i in range(0, len(message), key_length)]
    print(list_of_splited_litters)
    return list_of_splited_litters


def slice_each_letter_of_key(list_of_splited_litters, key_length):
    di = dict()
    i = 0
    for word in list_of_splited_litters:
        i = 0
        for letter in word:
            if i > key_length:
                i = 0
            s = di.get(i + 1, 0)
            if s == 0:
                di[i + 1] = [letter]
            else:
                di[i + 1] = di[i + 1] + [letter]
            i += 1
    print(di)
    return di
