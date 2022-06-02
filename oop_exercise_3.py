from collections.abc import Iterable, Generator

class LessThan():
    def __init__(self, n_list: Iterable) -> None:
        self.n_list = n_list

    @property
    def less_than_5(self) -> Generator:
        return (
            x for x in self.n_list if x<5
              )

    def less_than(self, input_number: int) -> Generator:
        return (
            x for x in self.n_list if x<input_number
              )

u_input = [1,2,3,4,5,6,7,8,9,10,11,12]
lt = LessThan(u_input)
print("less than 5? ",list(lt.less_than_5))
print("less than 11", list(lt.less_than(11)))

user_treshold = input("input custom treshold: ")
print(
    f"Custom list with treshold {user_treshold} is: ", 
    list(lt.less_than(int(user_treshold)))
    )
