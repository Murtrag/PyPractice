from __future__ import annotations
from abc import ABC, abstractmethod
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
    self._next_handler = handler
    return handler
    
  @abstractmethod  
  def handle(self, request: dict) -> Optional:
    print(self._next_handler)  
    if self._next_handler:
      return self._next_handler.handle(request)
    return None

class ExitHandler(AbstractAnsHandler):
  def handle(self, request: list) -> dict:
    print(request)
    if "exit" in request["answear"]:
      return {"aswear": "bye", "status": -1}
    return super().handle(request)
class BiggerHandler(AbstractAnsHandler):
  def handle(self, request: dict) -> dict:
    if int(request["answear"]) > int(request["guess"]):
      return {"aswear": "Too big!", "status": 1}
    return super().handle(request)
class SmallerHandler(AbstractAnsHandler):
  def handle(self, request: dict) -> dict:
    if int(request["answear"]) < int(request["guess"]):
      return {"aswear": "Too small!", "status": 1}
    return super().handle(request)
class EqualHandler(AbstractAnsHandler):
  def handle(self, request: dict) -> dict:
    if int(request["answear"]) == int(request["guess"]):
      return {"aswear": "Good job that is a correct answear!", "status": 0}
    return super().handle(request)

class RandomGame:
  def __init__(self) -> None:
    self.restart_guess_num()
    
  def is_correct(self, number: int):
    return number == self.guess_num
    
  def evaluate(self, answear: str) -> str:
      handler = ExitHandler()
      handler.set_next(BiggerHandler()).set_next(SmallerHandler()).set_next(EqualHandler())
      return handler.handle({
        "answear": answear,
        "guess": self.guess_num
      })
      
  
  def restart_guess_num(self) -> None:
    self.guess_num : int = random.randint(1,9)
    

      

def play():
  rg : RandomGame = RandomGame()
  while True:
      print("New game, try to guess a number from <1;9>")
      rg.restart_guess_num()
      while True:
        answear : str = input("What is your guess? ")
        evaluation: str = rg.evaluate(answear)
        if evaluation["status"] == 0:
          break
        if evaluation["status"] == -1:
          exit(0)
        print(evaluation["aswear"])

if __name__ == "__main__":
    play()




