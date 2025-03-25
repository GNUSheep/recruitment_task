from django.test import TestCase
from .checker import is_valid

# Create your tests here.
class CheckerTestCase(TestCase):
    def test_checker(self):
        tests = {
            "02070803628": (True, "08-07-1902", "female"),
            "99030528235": (True, "05-03-1999", "male"),
            "99030578941": (False, "Error: PESEL control numbers doesn't match with calculated one", ""),
            "940205518941": (False, "Error: PESEL should be 11 numbers long", ""),
            "99030578941a": (False, "Error: PESEL should only contains digits", ""),
        }
        

        for test, ans in tests.items():
            self.assertEqual(is_valid(test), ans)
