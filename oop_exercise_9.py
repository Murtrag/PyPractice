from __future__ import annotations
import random


class RandomGame:
  def __init__(self) -> None:
    self.restart_guess_num()
    
  def is_correct(self, number: int):
    return number == self.guess_num
    
  def evaluate(self, answear: str) -> str:
      pass
  
  def restart_guess_num(self) -> None:
    self.guess_num : int = random.randint(1,9)
    

      

def game():
  rg : RandomGame = RandomGame()
  while True:
      print("New game, try to guess a number from <1;9>")
      rg.restart_guess_num()
      while True:
        answear : str = input("What is your guess? ")
        evaluation: str = rg.evaluate(answear)
        if rg.is_correct(int(answear)):
          print("Good job that is a correct answear!")
          break
        print("Nop is ")

if __name__ == "__main__":
    game()




