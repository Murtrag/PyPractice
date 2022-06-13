import datetime

class HundredYear:
    def __init__(self, age: int, name="unknown") -> None:
        self.age = int(age)
        self.name = name
        
    def __get_hundred_diff(self, age: int) -> int:
        return 100 - self.age
    
    @property
    def __current_year(self) -> int:
        return datetime.date.today().year
    
    def get_target_year(self, age: int) -> int:
        return self.__current_year + self.__get_hundred_diff(self.age)
        
    def present(self, repeat: int=1) -> None:
        print(repeat*"{} will turn 100yr old in {} \n".format(
            self.name,
            self.get_target_year(self.age)
            ))
        
    
    def __repr__(self) -> None:
        return "HundredYear(self, {}. {})".format(age, name)

u_name = input("Input your name: ")
u_age = input("Input your age: ")

hundred_year = HundredYear(u_age, u_name)
hundred_year.present()

repeat = input("How many time repeat: ")
hundred_year.present(int(repeat))



