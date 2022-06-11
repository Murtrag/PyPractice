class PassGenContext:
    def __init__(self) -> None:
        self.__strategies = list()
        self.__password = ""

    @property
    def strategies(self) -> list:
        return self.__strategies

    @strategies.setter
    def set_strategies(self, strategies) -> None:
        self.__strategies = strategies

    def get_password(self) -> str:
        for strategy in self.__strategies:
            self.__password = strategy.transform_password(self.__password)
        return self.__password or "dupa"


#Strategies
import random

class Strategy:
    def __init__(self) -> None:
        pass

    def transform_password(self, password) -> str:
        print("tr", password)
        return password

class TextLength(Strategy):
    def __init_(self, length) -> None:
        pass
    def transform_password(self, password) -> str:
        return password + "length"

class TextChars(Strategy):
    def __init__(self, length) -> None:
        pass
    def transform_password(self, password) -> str:
        return password + "chars"

class TextPhrase(Strategy):
    def __init__(self, phrase) -> None:
        self.__phrase = phrase
        
    def __get_letters(self) -> str:
        return "".join([
            x[0] for x in self.__phrase.split(' ')
            ])
            
    def transform_password(self, password) -> str:
        pass_list = [password, self.__get_letters()]
        random.shuffle(pass_list)
        return "".join(pass_list)

class TextPokemon(Strategy):
    def __init__(self, step) -> None:
        self.__step = step
    
    def transform_password(self, password) -> str:
        return ''.join(
             x.upper() if i % self.__step == 0 else x.lower()  for i, x in enumerate(password)
             
        )
################################################################
class MainContext:
    __state: State = None
    __password_generator: PassGenContext = PassGenContext
    __prompt: str = ">> "

    @property
    def state(self) -> list:
        return self.__state

    @strategies.setter
    def set_state(self, state) -> None:
        self.__state = state
        
    def set_password(self) -> None:
        __state.perform()
        
    def select_object(self) -> None:
        __state.perform()
        
    def display_data(self) -> None:
        __state.perform()
        
#States
class MainState:
    _name: str = ""
    __context: MainContext = MainContext()

 
    def __init__(self) -> None:
        self.__prompt: str = ">> "

    def perform(self) -> None:
        print(f" --{name}-- ")
        

    
class SetState:
    __name = "Set State"
    def __init__(self) -> None:
        super().__init__(self)
    def perform(self) -> None:
        super().perform()
        pass

class SelectState: 
    __name = "Select State"
    def __init__(self) -> None:
        super().__init__(self)
    def perform(self) -> None:
        super().perform() 
        pass


class MenuState: 
    __name = "Menu State"
    def __init__(self) -> None:
        super().__init__(self) 
    def perform(self) -> None:
        super().perform()
        pass

class MenuFasade:
    


def app():
    prompt = ">> "
    while True:
        user_input = input(f"{prompt}")
        #Chain of responsibilities?
    
# State Set   
# help
# $ set password http://www.google.com
# choose strategies asdfasdfas
# $ 1356
# set length
# set pass phrase
# set ...

#State Modify

#Stat Select
# http://www.google.pl >> 

#State Menu
# $ show all
# select http://www.google.pl
# $ set password http://www.google.com




if __name__ == "__main__":
     pgc= PassGenContext()
     pgc.set_strategies= [
         TextChars(8),
         TextPhrase("krowi placek"),
         TextPokemon(3)
     ]
     print(
     pgc.get_password()
     )
