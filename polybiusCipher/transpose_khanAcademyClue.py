#this is sepecial version of polybiusCipher wich has no z and its transposed (rows become column)
def polybiusCipherEncrypt(s):
    encrypt = ""
    # convert each character to its encrypted code
    for char in s:

        # finding row of the table
        row = int((ord(char) - ord("a")) % 5) + 1

        # finding column of the table
        col = int((ord(char) - ord("a")) / 5) + 1

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
        ch = chr((c - 1) * 5 + r + 96)
        ch1 = str(ch)
        dec += ch1
    return dec


e = "44541134541123335344541242434244325141212311311353155442544244424344325141534354324234411125513553341342432253431144543453432251343142143251341253341215541534513351444411225144425442444415345123551543213451111311212351425431533321424351445315341434512542531544335154325341443"
out1 = polybiusCipherDecrypt(e)
print(out1)
