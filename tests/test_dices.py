from dices import *

def test_fun_1():
        res = int(roll())
        assert res >= 1 and res <= 6  
       
def test__fun_2():
        res = roll_again
        assert isinstance(res, str) == True
        
def test_fun_3():
        assert min_val == 1 and max_val == 6