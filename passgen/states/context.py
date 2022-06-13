class MainContext:
    __state: MainState = None
    __password_generator: PassGenContext = PassGenContext
    __prompt: str = ">> "

    @property
    def state(self) -> list:
        return self.__state

    @state.setter
    def state(self, state) -> None:
        self.__state = 