from .strategy import Strategy

class TextChars(Strategy):
    def __init__(self, length) -> None:
        pass
    def transform_password(self, password) -> str:
        return password + "chars"