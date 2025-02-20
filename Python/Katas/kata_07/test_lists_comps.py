import unittest
from lists_comps import *

class TestComprehensions(unittest.TestCase):

    def test_square_numbers(self):
        numbers = [1, 2, 3, 4, 5]
        result = square_numbers(numbers)
        expected = [1, 4, 9, 16, 25]
        self.assertEqual(result, expected)

    def test_even_numbers(self):
        numbers = [1, 2, 3, 4, 5, 6]
        result = even_numbers(numbers)
        expected = [2, 4, 6]
        self.assertEqual(result, expected)

    def test_uppercase_words(self):
        words = ['hello', 'world', 'python']
        result = uppercase_words(words)
        expected = ['HELLO', 'WORLD', 'PYTHON']
        self.assertEqual(result, expected)

    def test_flatten_list(self):
        nested_list = [[1, 2], [3, 4], [5, 6]]
        result = flatten_list(nested_list)
        expected = [1, 2, 3, 4, 5, 6]
        self.assertEqual(result, expected)

    def test_remove_none(self):
        my_list = [1, None, 2, None, 3, 4]
        result = remove_none(my_list)
        expected = [1, 2, 3, 4]
        self.assertEqual(result, expected)

    def test_first_character(self):
        words = ['apple', 'banana', 'cherry']
        result = first_character(words)
        expected = ['a', 'b', 'c']
        self.assertEqual(result, expected)

    def test_zip_lists(self):
        names = ['Alice', 'Bob', 'Charlie']
        scores = [85, 90, 88]
        result = zip_lists(names, scores)
        expected = [('Alice', 85), ('Bob', 90), ('Charlie', 88)]
        self.assertEqual(result, expected)

    def test_remove_duplicates(self):
        numbers = [1, 2, 2, 3, 4, 5, 5, 6]
        result = remove_duplicates(numbers)
        expected = [1, 2, 3, 4, 5, 6]
        self.assertEqual(result, expected)

    def test_long_words(self):
        words = ['apple', 'pie', 'banana', 'pear', 'grape']
        result = long_words(words)
        expected = ['apple', 'banana', 'grape']
        self.assertEqual(result, expected)

    def test_multiply_lists(self):
        list1 = [1, 2, 3, 4]
        list2 = [5, 6, 7, 8]
        result = multiply_lists(list1, list2)
        expected = [5, 12, 21, 32]
        self.assertEqual(result, expected)

    def test_non_negative_numbers(self):
        numbers = [-1, 2, -3, 4, 5, -6]
        result = non_negative_numbers(numbers)
        expected = [2, 4, 5]
        self.assertEqual(result, expected)

    def test_squared_evens(self):
        numbers = [1, 2, 3, 4, 5, 6]
        result = squared_evens(numbers)
        expected = [4, 16, 36]
        self.assertEqual(result, expected)

    def test_dict_values_to_str(self):
        my_dict = {1: 10, 2: 20, 3: 30}
        result = dict_values_to_str(my_dict)
        expected = {1: '10', 2: '20', 3: '30'}
        self.assertEqual(result, expected)

    def test_create_dict_from_lists(self):
        keys = ['name', 'age', 'city']
        values = ['Alice', 25, 'New York']
        result = create_dict_from_lists(keys, values)
        expected = {'name': 'Alice', 'age': 25, 'city': 'New York'}
        self.assertEqual(result, expected)

    def test_word_lengths(self):
        words = ['apple', 'banana', 'cherry']
        result = word_lengths(words)
        expected = {'apple': 5, 'banana': 6, 'cherry': 6}
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
