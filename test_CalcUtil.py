
import unittest
import module.LineMessage as lm
import module.CalcUtil as cu
import datetime


class TestCalcUtil(unittest.TestCase):
    """テストする"""

    #def setUp(self):
    #    print('setUp')

    def test_timeCheckMethod1(self):
        
        self.assertEqual(
        cu.checkIfPastSpecificTimeInSec(
        datetime.datetime(2017, 12, 28, 10, 5, 6, 620836),
        datetime.datetime(2017, 12, 28, 22, 5, 6, 620836),20)
        ,True)

    def test_timeCheckMethod2(self):
        self.assertEqual(
        cu.checkIfPastSpecificTimeInSec(
        datetime.datetime(2017, 12, 28, 22, 5, 6, 0),
        datetime.datetime(2017, 12, 28, 22, 35, 6, 0),20)
        ,True)

    def test_timeCheckMethod3(self):
        self.assertEqual(
        cu.checkIfPastSpecificTimeInSec(
        datetime.datetime(2017, 12, 28, 22, 5, 6, 0),
        datetime.datetime(2017, 12, 28, 22, 10, 6, 0),300)
        ,False) 

    def test_timeCheckMethod4(self):
        self.assertEqual(
        cu.checkIfPastSpecificTimeInSec(
        datetime.datetime(2017, 12, 28, 22, 5, 6, 0),
        datetime.datetime(2017, 12, 28, 22, 10, 6, 0),299)
        ,True)      
        #self.assertRaises(ValueError)
        #self.assertEqual(1,1)


    def test_checkIfHigerValueExist1(self):
        self.assertEqual(cu.checkIfHigerValueExist([24.5,24.0,23.9], 24),False)

    def test_checkIfHigerValueExist2(self):
        self.assertEqual(cu.checkIfHigerValueExist([24.5,24.0,23.9], 26),False)

    def test_checkIfHigerValueExist3(self):
        self.assertEqual(cu.checkIfHigerValueExist([24.5,24.0,23.9], 23),True)

    def test_checkIfHigerValueExist4(self):
        self.assertEqual(cu.checkIfHigerValueExist([24.5,26,23.9], 25),True)

    def test_checkIfLowerValueExist1(self):
        self.assertEqual(cu.checkIfLowerValueExist([24.5,24,23.9], 26),True)

    def test_checkIfLowerValueExist2(self):
        self.assertEqual(cu.checkIfLowerValueExist([24.5,25,23.9], 24),False)

if __name__ == '__main__':
    unittest.main()