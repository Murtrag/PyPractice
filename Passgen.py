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
            self.__passwrod = strategy.transform_password(self.__password)
        return self.__passwrod or "dupa"


#Strategies
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
        pass
    def transform_password(self, password) -> str:
        return password + "phrase"

class TextPokemon(Strategy):
    def __init__(self, boolean) -> None:
        pass
    def transform_password(self, password) -> str:
        return ''.join(
             x.upper() for i, x in enumerate(password)
             if i%2==0
        )

if __name__ == "__main__":
     pgc= PassGenContext()
     pgc.set_strategies= [
         TextChars(8),
         TextPhrase("krowi placek"),
         TextPokemon(2)
     ]
     print(
     pgc.get_password()
     )
