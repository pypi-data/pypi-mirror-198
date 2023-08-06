import unittest
from ColadaUtility.PowerColor import Colors as c

class ColorTest(unittest.TestCase):
    def test_foreground(self):
        self.assertEqual(c(f='r'), '\033[31m')
        
    def test_background(self):
        self.assertEqual(c(b='x'), '\033[;40m')
        
    def test_decorations(self):
        self.assertEqual(c(d='b i u s'), '\033[;1;3;4;9m')
        
    def test_text(self):
        self.assertEqual(c(f='y', b='b', d='u', t='test'), '\033[33;44;4mtest\033[0m')
        

if __name__ == '__main__':
    unittest.main()