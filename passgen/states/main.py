from .set import SetState
from .select import SelectState
from .menu import  MenuState
from .abstract import State

class MainState(State):
    _name: str = "" 
    def __init__(self, context, element="") -> None:
        self._prompt: str = ">> "
        #self._context = context

    @property
    def prompt(self) -> None:
        return self._prompt

    def perform(self, input_) -> None:
        #print(f" --{self._name}-- ")
        context = self._context
        if "set" in input_:
            self.transition_to(SetState(context))
            return True
        elif "select" in input_:
            self.transition_to(SelectState(context))
            return True
        elif "menu" in input_:
            self.transition_to(MenuState(context))
            return True
        else:
            return False