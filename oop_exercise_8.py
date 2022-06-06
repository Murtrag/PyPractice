 h random import choice                                            
                                                                   
 class RockPaperScissors:                                          
     points: int = 0                                               
     round_: int = 0                                               
     figures: dict = {                                             
         "rock": {                                                 
             "name": "rock",                                       
             "value": 0                                            
             },                                                    
         "paper":{                                                 
             "name": "paper",                                      
             "value": 1                                            
             },                                                    
         "scissors":{                                              
             "name": "scissors",                                   
             "value": 2                                            
             }                                                     
         }                                                         
                                                                   
     def __init__(self, rounds: int, difficulty: int) -> None:     
         self.rounds : int = rounds                                
         self.difficulty : int = difficulty                        
                                                                   
     @property                                                     
     @classmethod                                                  
     def __get_computer_move(cls) -> dict:                         
         return cls.figures[ choice(cls.figures.keys()) ]          
                                                                   
     def __check_winner(self, a_move : dict, b_move: dict) -> int: 
         if a_move["value"] == b_move["value"]:                    
             return 0                                              
         if a_move["value"] == 0 and b_move["value"] == "1":       
             return -1                                             
         if a_move["value"] == 0 and b_move["value"] == "2":       
             return 1                                              
         if a_move["value"] == 1 and b_move["value"] == "0":       
             return 1                                              
         if a_move["value"] == 1 and b_move["value"] == "2":       
             return -1                                             
         if a_move["value"] == 2 and b_move["value"] == "0":       
             return -1                                             
         if a_move["value"] == 2 and b_move["value"] == "1":       
             return 1                                              
                                                                   
                                                                   
                                                                   
 #FACTORY                                                          
 class FigureCreator:                                              
                                                                   
                                                                   
                                                                   
                                                                   
                                                                   
                                                                   
                                                                   
                                                                   
                                                                   
                                                                   
                                                                   
                                                                   
                                                                   
                                                                   
                                                                   
                                                                   
                                                                   
                                                                   
                                                                   
                                                                   
                                                                   
                                                                   
                                                                   
                                                                   
                                                                   
                                                                   
                                                                   
                                                                   
                                                                   
                                                                   
                                                                   
                                                                   
                                                                   
                                                                   
                                                                   
                                                                   
                                                                   
                                                                   
                                                                   
                                                                   
                                                                   
                                                                   
                                                                   
                                                                   
                                                                   
                                                                   
 if __name__ == "__main__":                                        
     rps = RockPaperScissors(3,)                                   
