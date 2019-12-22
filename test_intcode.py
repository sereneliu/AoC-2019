import unittest
import intcode

example_input = [1,9,10,3,2,3,11,0,99,30,40,50]

class IntcodeTestCase(unittest.TestCase):
  def test_intcode1(self):
    result = intcode.intcode(example_input, 0)
    self.assertEqual(result, 3500)
  
  def test_intcode2(self):
    result = intcode.intcode([1,0,0,0,99], 0)
    self.assertEqual(result, 2)
  
  def test_intcode3(self):
    result = intcode.intcode([2,3,0,3,99], 0)
    self.assertEqual(result, 2)
    
  def test_intcode4(self):
    result = intcode.intcode([2,4,4,5,99,0], 0)
    self.assertEqual(result, 2)
  
  def test_intcode5(self):
    result = intcode.intcode([1,1,1,4,99,5,6,0,99], 0)
    self.assertEqual(result, 30)

if __name__ == '__main__':
  unittest.main()
