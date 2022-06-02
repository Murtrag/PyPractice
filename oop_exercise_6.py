import re

class Palindrome:
    def __init__(self, text:str) -> None:
        self.text :str = text

    def __strip_redundand(self, text: str) -> str:
        return re.sub("\W{1}", "", text)
    
    def is_palindrome(self, strip_redundand=True):
        if strip_redundand:
            striped_text: str = self.__strip_redundand(
                self.text
            )
            return striped_text == striped_text[::-1]
        return self.text == self.text[::-1]

if __name__ == "__main__":
    palindrome = Palindrome("ala v ala")
    print(
        palindrome.is_palindrome(False)
        )
