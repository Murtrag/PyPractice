from __future__ import annotations
from abc import ABC, abstraction
from typing import Any, Optional

import random

class AnsHandler:
  @abstractmethod
  def set_next(self, handler: AnsHandler) -> AnsHandler:
    pass
  
  @abstractmethod
  def handle(self, request: dict) -> Optional:
    pass
  
class AbstractAnsHandler(AnsHandler):
  _next_handler: AnsHandler = None
    
  def set_next(self, handler: AnsHandler) -> AnsHandler:
    AbstractAnsHandler._next_handler = handler
    return handler
    
  def handle(self, request: dict) -> Optional:
    if AbstractAnsHandler._next_handler:
      retrun AbstractAnsHandler._next_handler.handle(request)
    return None

class ExitHandler(AbstractAnsHandler):
  def handle(self, request: list) -> None:  # request should contain two values to compare values
    if "exit" in request["answear"]:
      return "exit"
    return super().handle(request)
class BiggerHandler(AbstractAnsHandler):
  def handle(self, request: dict) -> None:
    if request["answear"] > request["guess"]:
      return "Too big!"
    return super().handle(request)
class SmallerHandler(AbstractAnsHandler):
  def handle(self, request: dict) -> None:
    if request["answear"] > request["guess"]:
      return "Too small!"
    return super().handle(request)
class EqualHandler(AbstractAnsHandler):
  def handle(self, request: dict) -> None:
    if request["answear"] == request["guess"]:
      return "Good job that is a correct answear!"
    return super().handle(request)

class RandomGame:
  def __init__(self) -> None:
    self.restart_guess_num()
    
  def is_correct(self, number: int):
    return number == self.guess_num
    
  def evaluate(self, answear: str) -> str:
      handler = ExitHandler().set_next(BiggerHandler).set_next(SmallerHandle).set_next(EqualHandle)
      handler.handle({
        "answear": answear,
        "guess": self.guess_num
      })
      
  
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




