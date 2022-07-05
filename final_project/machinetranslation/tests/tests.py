import unittest
from translator import english_to_french, french_to_english


class Test_E2F(unittest.TestCase):
    def test1(self):
        self.assertEqual(english_to_french("Hello"),"Bonjour")
        self.assertNotEqual(english_to_french("Hola"),"Bonjour")
        self.assertIsNotNone(self)

class Test_F2E(unittest.TestCase):
    def test2(self):
        self.assertEqual(french_to_english("Bonjour"),"Hello")
        self.assertNotEqual(french_to_english("Gracias"),"Hello")
        self.assertIsNotNone(self)

unittest.main() 
