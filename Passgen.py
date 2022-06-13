from __future__ import annotations
db = {}
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

#States
class MainState:
    _name: str = "" 
    def __init__(self, context, element="") -> None:
        self._prompt: str = ">> "
        self._context = context

    @property
    def prompt(self) -> None:
        return self._prompt

    def perform(self, input_) -> None:
        #print(f" --{self._name}-- ")
        context = self._context
        if "set" in input_:
            self._context.state = SetState(context)
            return True
        elif "select" in input_:
            self._context.state = SelectState(context)
            return True
        elif "menu" in input_:
            self._context.state = MenuState(context)
            return True
        else:
            return False
        
    

class SetState(MainState):
    _name = "Set State"
    
    def __init__(self, context, element="") -> None:
        super().__init__(context, element)
        self._prompt: str = f"({element})>> "
        
    @property
    def prompt(self) -> None:
        return self._prompt
    
    @prompt.setter
    def prompt(self, prompt) -> None:
        self._prompt = prompt
    	
    def __set_password(self) -> None:
        try:
          print("Set password")
          input_ = input(f"{self.prompt} >> ")
          db[self.prompt] = input_ 
        except Exception as err:
          print(f"Get unexpected error: \n {err}")

    def __set_target(self) -> None:
        try:
          print("Set target")
          input_ = input(">> ")
          self.prompt = input_
        except Exception as err:
          print(f"Get unexpected error: \n {err}")

    def perform(self, input_) -> None:
        super().perform(input_)
        self.__set_target()
        self.__set_password()
        print('password has been created')
        self._context.state =  MenuState(self._context)

class SelectState(MainState):    
    _name = "Select State"
  
    def __init__(self, context, element) -> None:
        self.__prompt: str = f"({element})>> "
        super().__init__(self)
    
    @property
    def prompt(self) -> None:
        return self._prompt
        
    def perform(self, input_) -> None:
        super().perform(input_) 


class MenuState(MainState): 
    __name = "Menu State"
    def __init__(self, context, element="") -> None:
        super().__init__(context, element)
        self._prompt: str = ">> "
         
    @property
    def prompt(self) -> None:
        return self._prompt    
        
    def perform(self, input_) -> None:
        is_performed = super().perform(input_)
        if is_performed is True:
          return          
        if "list" in input_:
          pprint(db)
        elif "help" in input_:
          print("help")
        else:
          print("invalid syntax")        
        
class MainContext:
    __state: MainState = None
    __password_generator: PassGenContext = PassGenContext
    __prompt: str = ">> "

    @property
    def state(self) -> list:
        return self.__state

    @state.setter
    def state(self, state) -> None:
        self.__state = state
        
        

def fasade():
    mc = MainContext()
    mc.state = MenuState(mc)
    while True:
        user_input = input(f"{mc.state.prompt}")
        mc.state.perform(user_input)
    
if __name__ == "__main__":
     #pgc= PassGenContext()
     #pgc.set_strategies= [
     #    TextChars(8),
     #    TextPhrase("krowi placek"),
     #    TextPokemon(3)
     #]
     #print(
     #pgc.get_password()
     #)
     fasade()
