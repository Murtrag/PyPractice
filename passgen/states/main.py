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
        pass