class PassGenContext:
    def __init__(self) -> None:
        self.__strategies = list()

    @property
    def strategies(self) -> list:
        return self.__strategies

    @strategies.setter
    def set_strategies(self, strategies) -> Strategy:
        self.__strategies = strategies

    def get_password(self) -> str:
        for strategy in self.__strategies:
            strategy.transform_password(pass)
        return pass


#Strategies
class Strategy:
    def __init__(self) -> None
        pass

    def transform_password(self, pass) -> str:
        return password

class TextLength(Strategies):
    def __init_(self, length) -> None:
        password

class TextChars(Strategies):
    def __init__self, length) -> None:
        password

class TextPhrase(Strategies):
    def __init_(self, length) -> None:
        pass

 class TextPokemon(Strategy):
    def __init__(self) -> None:
        pass
    def transform_password(self, password) -> str:
        return ''.join(
             x.upper() for i, x in enumerate(password)
             if i%2==0
        )

if __name__ == "__main__":
     pgc= PassGenContext()
     pgc.set_strategies(
         TextChars(8),
         TextPhrase("krowi placek"),
         TextPokemon(2)
     )
     pgc.get_password()
