from __future__ import annotations

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

#States
class MainState:
    _name: str = ""
    

 
    def __init__(self, context, element="") -> None:
        print("init super variables")
        self._prompt: str = ">> "
        self._context = context
        print("self context in super ", self._context)
        
    @property
    def prompt(self) -> None:
        return self.__prompt

    def perform(self, input_) -> None:
        print(f" --{self._name}-- ")
        state = MenuState(self._context)
        if "set" in input_:
            state = SetState()
        if "select" in input_:
            state = SelectState()
        if "menu" in input_:
            state = MenuState()
        self._context.state = state
    

class SetState(MainState):
    _name = "Set State"
    
    def __init__(self) -> None:
        super().__init__(self)
        self.__prompt: str = "()>> "
        
        
    def set_target(self):
    	#set name of target password
    	#set and change prompt
    	pass
    
    @property
    def prompt(self) -> None:
        return self.__prompt
    	
    def set_password(self) -> None: 
        #ask and set password 
        pass
        
    def perform(self, input_) -> None:
        super().perform(input_)
        pass

class SelectState(MainState): 
    
    _name = "Select State"
    def __init__(self, context, element) -> None:
        self.__prompt: str = f"({element})>> "
        super().__init__(self)
    
    @property
    def prompt(self) -> None:
        return self.__prompt
        
    def perform(self, input_) -> None:
        super().perform(input_) 
        pass


class MenuState(MainState): 
    __name = "Menu State"
    def __init__(self, context, element="") -> None:
        print('goto parent')
        super().__init__(context, element)
        print('backto child')
        #self.__context = context
        #print(self._prompt)
        self._prompt: str = ">> "
         
    @property
    def prompt(self) -> None:
        return self._prompt
    
        
    def perform(self, input_) -> None:
        super().perform(input_)
        print(self._context)


        
        
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
        
    def set_password(self) -> None:
        __state.perform()
        
    def select_object(self) -> None:
        __state.perform()
        
    def display_data(self) -> None:
        __state.perform()
        


class MenuFasade:
    mc = MainContext()
    def run(self):
        while True:
            user_input = input(f"{prompt}")
            


def app():
    mc = MainContext()
    mc.state = MenuState(mc)
    while True:
        user_input = input(f"{mc.state.prompt}")
        mc.state.perform(user_input)
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
     app()
