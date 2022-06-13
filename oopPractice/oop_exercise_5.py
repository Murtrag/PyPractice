from collections.abc import Generator

class Overlaps:
    def __init__(self, list_1, list_2) -> None:
        self.list_1: list = list_1
        self.list_2: list = list_2
    
    def get_overlaps(self) -> set:
        return set(self.list_1).intersection(set(self.list_2))
    
    def present(self) -> None:
        print("Overlaps are: ")
        for x in self.get_overlaps():
            print(f"- {x}")

o = Overlaps([1,2,3,4,5,6,7,8], [11,10,9,8, 111, 7])

o.present()
