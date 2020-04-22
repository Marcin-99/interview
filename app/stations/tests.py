import unittest
from utilities import is_int, is_float, look_for_duplicates


class TestFunctions(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('Test: start')
        print("\n")

    @classmethod
    def tearDownClass(cls):
        print("\n")
        print('Test: finished')

    def test_is_int(self):
        example = "number"
        input = is_int(example)
        expected_output = False
        self.assertEqual(input, expected_output)

        example = 1
        input = is_int(example)
        expected_output = True
        self.assertEqual(input, expected_output)

    def test_is_float(self):
        example = ["one", 2, 3, 4, 5]
        input = is_float(example)
        expected_output = False
        self.assertEqual(input, expected_output)

        example = [3.14, 2.72]
        input = is_float(example)
        expected_output = True
        self.assertEqual(input, expected_output)

        example = ["", 2.72, "", 3.14]
        input = is_float(example)
        expected_output = True
        self.assertEqual(input, expected_output)


if __name__ == '__main__':
    unittest.main()