from .main import MainState

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