Copyright © 2021 Elshe2



"""
1- calculte index of concidence (IC)
    sum(fi*(fi-1))/N(N-1)
2-english lang has ci 0.065 this mean if ci is close to this number that mean the cipher been used is monoalphapetic cipher
if the ic is between 0.0385 and 0.065 that mean the cipher been used is most likely polyalphapetic cipher 

"""
class Friedman_crack:
    def __init__(self, message):
        self.message = message
        self.li = []
        self.di = {}
        self.message_length = len(self.message)
        self.ic = 0
        self.key_length = 0
        self.convert_text_to_numbers()
        self.cla_frequency()
        self.cal_IC()

    def convert_text_to_numbers(self):
        message = self.message.lower()
        for letter in message:
            num = ord(letter) - ord("a") + 1
            self.li.append(num)

    def cla_frequency(self):
        li = self.li
        for num in li:
            num = str(num)
            s = self.di.get(num, 0)
            if s == 0:
                self.di[num] = 1
            else:
                self.di[num] = self.di[num] + 1

    def cal_IC(self):
        sum = 0
        for i in self.di.values():
            sum += i * (i - 1)
        ic = sum / (self.message_length * (self.message_length - 1))
        self.ic = ic

    def get_key_len(self):
        """
        key_len Friedman foruml is
        l= 0.0027n/(n-1)IC -0.038n+0.0065
        """
        x = 0.027 * self.message_length
        y = (self.message_length - 1) * self.ic - (0.038 * self.message_length) + 0.065
        key_length = x / y
        key_length = int(key_length)
        self.key_length = key_length
        return key_length

    def get_cihper_type(self):
        if 0.0385 <= self.ic < 0.065 and self.key_length > 1:
            print("its most likely a polyalphapetic cipher")
        else:
            print("its most likely a monoalphapetic cipher")

