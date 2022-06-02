class LessThan():
    def __init__(self, n_list: iter):
        self.n_list = n_list

    @prooerty
    def less_than_5(self):
        return (
            x for x in self.n_list if x<5
              )

    def less_than(self, input_number):
        return (
            x for x in self.n_list if x<input_number
              )

u_input = [1,2,3,4,5,6,7,8,9,10,11,12]
lt = LessThan(u_input)
print("less than 5? ",lt.less_than_5)
print("less than 11", lt.less_than(11))
