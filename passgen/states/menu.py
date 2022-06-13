from .main import MainState

from .select import SelectState
from .set import SetState
from .abstract import State

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
        context = self._context
        if "set" in input_:
            self.context.transition_to(SetState)            
            #self.context.state.perform(input_)
            return
        elif "select" in input_:
            self.transition_to(SelectState)
            return
        elif "menu" in input_:
            self.transition_to(MenuState)
        elif "list" in input_:
          print(db)
        elif "help" in input_:
          print("help")
        else:
          print("invalid syntax")    