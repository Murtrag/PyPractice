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
    state: State = None
    password_generator: PassGenContext= PassGenContext
    def create_password(self) -> sth:
        pass
    def 



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
