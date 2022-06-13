from collections.abc import Generator

class Divisors:
    def __init__(self, number: int) -> None:
        self.number: int = number
    
    def get_divisors(self) -> Generator:
            return (
                x for x in range(1, self.number)
                if self.number%x == 0
                )
    
    def present_divisors(self) -> None:
        print(f"Number {self.number} is divisible by: ")
        for divisor in self.get_divisors():
            print(f"- {divisor}")
            
divisor = Divisors(222)
divisor.present_divisors()
