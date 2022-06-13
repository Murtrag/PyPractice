from .main import MainState

db = {}

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
          print(db)
        elif "help" in input_:
          print("help")
        else:
          print("invalid syntax")    