    def test1(self):
        res = int(test.roll())
        assert res >= 1 and res <= 6  
        
    def test2(self):
        res = test.roll_again
        assert isinstance(res, str) == True
        
        
    def test3(self):
        assert min_val == 1 and max_val == 6