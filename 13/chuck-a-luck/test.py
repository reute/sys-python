import unittest

from chuck_a_luck import wuerfeln, berechneGewinn

class Test(unittest.TestCase):
    # Tests that a number between 1 and 6 is returned
    def test_wuerfeln(self):
        result = wuerfeln()        
        self.assertTrue(result > 0 and result < 7)
    def test_berechneGewinn(self):
        gewinn = berechneGewinn( [1,2,3], 1, 20 )
        self.assertEqual(gewinn, 20)

if __name__ == '__main__':
    unittest.main()


'''
pytest
from chuck_a_luck_func import wuerfeln, berechneGewinn

 def test_wuerfeln():
    result = wuerfeln()
    assert result > 0 and result < 7
'''
