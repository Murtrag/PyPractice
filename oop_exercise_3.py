class LessThan():
    def __init__(self):
        self.num = num

    @prooerty
    def less_than_5(self):
        return self.num<5

    def less_than(self, input_number):
        return self.num < input_number

u_input = input("input number to check")
lt = LessThan(209)
print("is less than 5? ",lt.less_than_5)
print("is less than 11", lt.less_than(11))
