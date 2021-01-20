import unittest
from  base_convert import *

class TestBaseConvert(unittest.TestCase):

    def test_base_less_than_10(self):
        self.assertEqual(convert(45,2),"101101")
        self.assertEqual(convert(0,2), '0')
        self.assertEqual(convert(110,3),"11002")
        self.assertEqual(convert(30,4),"132")
        self.assertEqual(convert(254,5),"2004")
        self.assertEqual(convert(276,6),"1140")
        self.assertEqual(convert(509,7),"1325")
        self.assertEqual(convert(104,8),"150")
        self.assertEqual(convert(11,9),"12")

    def test_base_more_than_10(self):
        self.assertEqual(convert(316,16),"13C")
        self.assertEqual(convert(413,15),"1C8")
        self.assertEqual(convert(534,14),"2A2")
        self.assertEqual(convert(312,13),"1B0")
        self.assertEqual(convert(124,12),"A4")
        self.assertEqual(convert(301,11),"254")

    def test_base_large_converts(self):
        self.assertEqual(convert(100000000,6),"13531202544")
        self.assertEqual(convert(299988913,4),'101320113132301')
        self.assertEqual(convert(7341213456,13),'8CCC039B5')
        self.assertEqual(convert(1235423345,16),'736D6565')

if __name__ == "__main__":
        unittest.main()