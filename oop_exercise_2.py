from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Optional, Any

class Handler(ABC):
    @abstractmethod
    def set_next(self, handler: Handler) -> Handler:
        pass
    
    @abstractmethod
    def handle(self, request) -> Optional[str]:
        pass

class AbstractHandler(Handler):
    _next_handler: Handler = None
    
    def set_next(self, handler: Handler) -> Handler:
        self._next_handler = handler
        return handler
        
    def handle(self, request: int) -> str:
        print(self._next_handler)
        if self._next_handler:
            return self._next_handler.handle(request)
        return None
        
class OddHandler(AbstractHandler):
    def handle(self, request: Any) -> str:
        if request%2 != 0:
            return f"The number {request} is odd"
        else:
            return super().handle(request)

class EvenHandler(AbstractHandler):
    def handle(self, request: Any) -> str:
        if request%2 == 0:
            return f"The number {request} is even"
        else:
            return super().handle(request)            

class FourMultipleHandler(AbstractHandler):
    def handle(self, request: Any) -> str:
        if request%4 == 0:
            return f"The number {request} is dividable by 4"
        else:
            return super().handle(request)    

odd_h = OddHandler()
even_h = EvenHandler()
four_m_h = FourMultipleHandler()

four_m_h.set_next(even_h).set_next(odd_h)

number = input("Input number to check: ")

print(
    four_m_h.handle(int(number))
    )

number2 = input('Input number2 to check: ')

print(
    even_h.handle(int(number)/int(number2))
    )

    
    
    
    
    
    
            
            
            
            
            
            
            
            
            
