
import unittest


def calculator(x,y):
    return x+y

def loler(x, y):
    return x*y

class Test_calculator(unittest.TestCase):
    
    def test_sum(self):
        self.assertEqual(10, calculator(5,5))
    
    def test_minus(self):
        self.assertEqual(10, calculator(-10,20))

    # Continue for calculator tests.

class Test_loler(unittest.TestCase):
    
    def test_sum(self):
        self.assertEqual(25, loler(5,5))
    
    def test_minus(self):
        self.assertEqual(-200, loler(-10,20))
    
    def test_greatertest(self):
        self.assertGreater(100, loler(100,2), msg = 'Something went wrong!')



if __name__ == "__main__":
    unittest.main()


    