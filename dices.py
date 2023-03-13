import random
import unittest

global min_val, max_val
min_val = 1
max_val = 6
roll_again = "yes"
    
def roll():
    return random.randint(min_val, max_val)


print("Rolling The Dices...")
print("The Values are :")
print(roll())
        
""""
while roll_again == "yes" or roll_again == "y":
    print("Rolling The Dices...")
    print("The Values are :")
    print(roll())
    roll_again = input("Roll the Dices Again? : ")
    if roll_again == "no" or "n":
        break

if __name__ == '__main__':
    unittest.main()
"""
    


        

    
  

        
   