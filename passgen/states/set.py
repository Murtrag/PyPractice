from main import MainState

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