import checker
import os
import unittest

class Test_TestLists(unittest.TestCase):
    def test_check_case(self):
        for filename in os.listdir('list'):
            file = open("./list/" + filename, encoding='utf-8')
            self.assertEqual(checker.check_case(file), "PASS")

    def test_check_double(self):
        for filename in os.listdir('list'):
            file = open("./list/" + filename, encoding='utf-8')
            assert checker.check_double(file) == "PASS"


if __name__ == '__main__':
    unittest.main()
