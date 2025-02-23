import unittest
from mock_lists import *

class TestMockExam(unittest.TestCase):

    # Test for Question 1: Data Structures
    def test_get_unique_values(self):
        data = [1, 2, 2, 3, 4, 4, 4]
        expected = {1: 1, 2: 2, 3: 1, 4: 3}
        self.assertEqual(get_unique_values(data), expected)

    # Test for Question 2: Data Manipulation
    def test_filter_positive_numbers(self):
        numbers = [-10, 0, 5, -3.5, 7.2]
        expected = [5, 7.2]
        self.assertEqual(filter_positive_numbers(numbers), expected)

    # Test for Question 3: Validations
    def test_validate_email(self):
        self.assertTrue(validate_email("test@example.com"))
        self.assertFalse(validate_email("invalid@@example.com"))
        self.assertFalse(validate_email("test@.com"))
        self.assertFalse(validate_email("test@example"))

    # Test for Question 4: Control Structures
    def test_find_max_value(self):
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        expected = 9
        self.assertEqual(find_max_value(matrix), expected)

    # Test for Question 5: Algorithmic Thinking
    def test_is_palindrome(self):
        self.assertTrue(is_palindrome("A man a plan a canal Panama"))
        self.assertFalse(is_palindrome("Hello World"))
        self.assertTrue(is_palindrome("racecar"))
        self.assertFalse(is_palindrome("palindrome"))

    # Test for Question 6: Advanced Data Structures
    def test_flatten_nested_list(self):
        nested_list = [1, [2, [3, 4], 5], 6]
        expected = [1, 2, 3, 4, 5, 6]
        self.assertEqual(flatten_nested_list(nested_list), expected)

    # Test for Question 7: Algorithmic Thinking
    def test_longest_common_prefix(self):
        strs = ["flower", "flow", "flight"]
        expected = "fl"
        self.assertEqual(longest_common_prefix(strs), expected)

    # Test for Question 8: Control Structures
    def test_count_primes(self):
        n = 10
        expected = 4
        self.assertEqual(count_primes(n), expected)

    # Test for Question 9: Advanced Algorithmic Thinking
    def test_merge_sorted_arrays(self):
        arr1 = [1, 3, 5]
        arr2 = [2, 4, 6]
        expected = [1, 2, 3, 4, 5, 6]
        self.assertEqual(merge_sorted_arrays(arr1, arr2), expected)

    # Test for Question 10: Recursion
    def test_fibonacci(self):
        n = 5
        expected = 5
        self.assertEqual(fibonacci(n), expected)

    # Test for Question 11: Graph Traversal
    def test_bfs(self):
        graph = {'A': ['B', 'C'], 'B': ['A', 'D'], 'C': ['A'], 'D': ['B']}
        start_node = 'A'
        expected = ['A', 'B', 'C', 'D']
        self.assertEqual(bfs(graph, start_node), expected)

    # Test for Question 12: Dynamic Programming
    def test_coin_change(self):
        coins = [1, 2, 5]
        amount = 11
        expected = 3
        self.assertEqual(coin_change(coins, amount), expected)

if __name__ == "__main__":
    unittest.main()