from Calc import Calc
import unittest

class TestFun(unittest.TestCase):
    def setUp(self):
        self.obj=Calc()
        print 'start'

    def test_add(self):
        self.assertEqual(self.obj.add(1,2,3),6)

    def test_sub(self):
        self.assertEqual(self.obj.sub(1,2,3),-4)

    def test_mul(self):
        self.assertEqual(Calc.mul(1,2,3),6)

    def test_div(self):
        self.assertEqual(self.obj.div(4,2,1),6)

    def tearDown(self):
        print 'done'

if __name__ == '__main__':
    unittest.main()