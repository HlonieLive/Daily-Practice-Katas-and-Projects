# test_mock_test.py

import unittest
from assessment_prep import (
    reverse_string_recursive,
    Stack,
    is_prime,
    factorial_iterative,
    get_user_input,
    generate_pascals_triangle,
    print_right_angled_triangle,
    print_pyramid,
    print_square,
)

class TestMockTest(unittest.TestCase):

    # Test reversing a string using recursion
    def test_reverse_string_recursive(self):
        self.assertEqual(reverse_string_recursive("hello"), "olleh")
        self.assertEqual(reverse_string_recursive("a"), "a")
        self.assertEqual(reverse_string_recursive(""), "")

    # Test stack implementation
    def test_stack(self):
        stack = Stack()
        self.assertTrue(stack.is_empty())
        stack.push(10)
        stack.push(20)
        self.assertFalse(stack.is_empty())
        self.assertEqual(stack.peek(), 20)
        self.assertEqual(stack.pop(), 20)
        self.assertEqual(stack.pop(), 10)
        self.assertTrue(stack.is_empty())

    # Test prime number checker
    def test_is_prime(self):
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(13))
        self.assertFalse(is_prime(1))
        self.assertFalse(is_prime(4))
        self.assertFalse(is_prime(10))

    # Test factorial calculation using iteration
    def test_factorial_iterative(self):
        self.assertEqual(factorial_iterative(0), 1)
        self.assertEqual(factorial_iterative(1), 1)
        self.assertEqual(factorial_iterative(5), 120)

    # Test user input validation (mocking input for testing)
    def test_get_user_input(self):
        # Mock user input for testing
        import builtins
        original_input = builtins.input
        try:
            builtins.input = lambda _: "123"  # Simulate user entering "123"
            self.assertEqual(get_user_input(), 123)
            builtins.input = lambda _: "abc"  # Simulate invalid input
            with self.assertRaises(ValueError):  # Expect a ValueError for invalid input
                get_user_input()
        finally:
            builtins.input = original_input

    # Test Pascal's Triangle generation
    def test_generate_pascals_triangle(self):
        self.assertEqual(generate_pascals_triangle(0), [])
        self.assertEqual(generate_pascals_triangle(1), <button class="citation-flag" data-index="1">)
        self.assertEqual(generate_pascals_triangle(2), [[1], [1, 1]])
        self.assertEqual(generate_pascals_triangle(3), [[1], [1, 1], [1, 2, 1]])
        self.assertEqual(generate_pascals_triangle(4), [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]])

    # Test right-angled triangle pattern
    def test_print_right_angled_triangle(self):
        import io
        import sys
        captured_output = io.StringIO()
        sys.stdout = captured_output
        print_right_angled_triangle(3)
        sys.stdout = sys.__stdout__
        expected_output = "*\n**\n***\n"
        self.assertEqual(captured_output.getvalue(), expected_output)

    # Test pyramid pattern
    def test_print_pyramid(self):
        import io
        import sys
        captured_output = io.StringIO()
        sys.stdout = captured_output
        print_pyramid(3)
        sys.stdout = sys.__stdout__
        expected_output = "  *\n ***\n*****\n"
        self.assertEqual(captured_output.getvalue(), expected_output)

    # Test square pattern
    def test_print_square(self):
        import io
        import sys
        captured_output = io.StringIO()
        sys.stdout = captured_output
        print_square(3)
        sys.stdout = sys.__stdout__
        expected_output = "***\n***\n***\n"
        self.assertEqual(captured_output.getvalue(), expected_output)

if __name__ == "__main__":
    unittest.main()