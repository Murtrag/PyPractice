import random

class RandomGame:
  def __init__(self) -> None:
    self.restart_guess_num()
    
  def is_correct(self, number: int):
    return number == self.guess_num
  
  def restart_guess_num(self) -> None:
    self.guess_num : int = random.randint(1,9)
      

def game():
  rg : RandomGame = RandomGame()
  print("New game, try to guess a number from <1;9>")
  while True:
    number : int = int(input("What is your guess? "))
    if rg.is_correct(number):
      print("Good job that is a correct answear!")
    print("Nop is ")
      
    
    
    
    
    
    
# New game, try to guess a number from <1;9>
#What is your guess? 4
#Nop is too small
#...

