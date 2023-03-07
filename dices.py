import random
import unittest

class test:
    global min_val, max_val
    min_val = 1
    max_val = 6
    roll_again = "yes"
    
    def roll():
        return random.randint(min_val, max_val)

    while roll_again == "yes" or roll_again == "y":
        print("Rolling The Dices...")
        print("The Values are :")
        print(roll())
        roll_again = input("Roll the Dices Again? : ")
        if roll_again == "no" or "n":
            break
        
    
    
class TestUnitaire(unittest.TestCase):

    def test1(self):
        res = int(test.roll())
        assert res >= 1 and res <= 6  
        
    def test2(self):
        res = test.roll_again
        assert isinstance(res, str) == True
        
    def test3(self):
        assert min_val == 1 and max_val == 6
    
if __name__ == '__main__':
    unittest.main()
        
        
        
        
        
        