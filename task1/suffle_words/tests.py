from django.test import TestCase
from .suffle_app import Parser

# Create your tests here.
class ParserTestCase(TestCase):
    def test_parser(self):
        tests = {
            "abc def-ghi": [("abc", " "), ("def", "-"), ("ghi", "")],
            "Hello\u2003world!": [("Hello", "\u2003"), ("world", "!")],            
            "ałćąw źćż": [("ałćąw", " "), ("źćż", "")]
        }
        
        parser = Parser()

        for test, ans in tests.items():
            self.assertEqual(parser.split(test), ans)
