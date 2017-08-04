#-*-coding:utf8;-*-
#qpy:3
#qpy:console
import unittest

import os 
import sys 
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))) 

import sameendfinder

testFunction = sameendfinder.sameEnds

class SameEndFinderTest(unittest.TestCase):
    def test_singlechar(self):
        """
        case: single char
        """
        inputStr ="Z"
        outputStr = "we need a longer input"
        self.assertEqual(outputStr,testFunction(inputStr))
    
    def test_leng2_nomatch(self):
        """
        case: leng=2
        """
        inputStr ="12"
        outputStr = "no same ends found"
        self.assertEqual(outputStr,testFunction(inputStr))
    
    def test_leng2_match(self):
        """
        case: leng=2
        """
        inputStr ="11"
        outputStr = "result:1"
        self.assertEqual(outputStr,testFunction(inputStr))
    
    def test_leng3_nomatch(self):
        """
        case: leng=3
        """
        inputStr ="123"
        outputStr = "no same ends found"
        self.assertEqual(outputStr,testFunction(inputStr))
    
    def test_leng3_match(self):
        """
        case: leng=3
        """
        inputStr ="121"
        outputStr = "result:1"
        self.assertEqual(outputStr,testFunction(inputStr))
    
    def test_alphanumeric(self):
        """
        case: alpha numeric value
        """
        inputStr ="qwerty123qwerty1"
        outputStr = "result:qwerty1"
        self.assertEqual(outputStr,testFunction(inputStr))
    
    def test_numeric(self):
        """
        case: numeric value
        """
        inputStr ="1234512345"
        outputStr = "result:12345"
        self.assertEqual(outputStr,testFunction(inputStr))
    
    def test_numeric_nosameend(self):
        """
        case: numeric value
        """
        inputStr ="123412345"
        outputStr = "no same ends found"
        self.assertEqual(outputStr,testFunction(inputStr))
    
    def test_repeat(self):
        """
        case: repeating text
        """
        inputStr ="qwqwqw"
        outputStr = "result:qw"
        self.assertEqual(outputStr,testFunction(inputStr))
    
    def test_SpChar(self):
        """
        case: special characters
        """
        inputStr ="$$%%:$$%%"
        outputStr = "result:$$%%"
        self.assertEqual(outputStr,testFunction(inputStr))
    
    def test_nosameend(self):
        """
        case: zero
        """
        inputStr ="qwerty123qwertyy"
        outputStr = "no same ends found"
        self.assertEqual(outputStr,testFunction(inputStr))
    
if __name__=='__main__':
    unittest.main(verbosity=2)