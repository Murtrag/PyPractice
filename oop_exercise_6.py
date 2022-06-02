import re

class Palindrome:
    def __init___(self, text:str) -> None:
        self.text :str = text

    def __strip_redundand(self, text: str) -> str:
        return re.sub("\A{1}", "", text)

    @property
    def is_palindrome(self):
        striped_text: str = self.__strip_redundand(
            self.text
        )
        return
