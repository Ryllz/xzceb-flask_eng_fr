import unittest
from translator import english_to_french, french_to_english

class testEnglishToFrench(unittest.TestCase): 
    # Null test
    def test1(self): 
        self.assertNotEqual(english_to_french(None), None)
    # Hello input test
    def test2(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour')

class testFrenchToEnglish(unittest.TestCase): 
    # Null test
    def test1(self): 
        self.assertNotEqual(french_to_english(None), None)
    # Bonjour inpuit test
    def test2(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello')

unittest.main()