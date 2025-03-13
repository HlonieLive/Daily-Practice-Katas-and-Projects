import unittest
from prep_quiz import *


class TestPracticeQuiz(unittest.TestCase):
    def test_student_initialization(self):
        student = Student("Alice", 20)
        self.assertEqual(student.name, "Alice")
        self.assertEqual(student.age, 20)
        self.assertEqual(student.grades, [])

    def test_get_positive_integer_valid(self):
        with unittest.mock.patch('builtins.input', return_value="42"):
            result = get_positive_integer()
            self.assertEqual(result, 42)

    def test_find_common_elements(self):
        list1 = [1, 2, 3, 4, 5]
        list2 = [4, 5, 6, 7, 8]
        result = find_common_elements(list1, list2)
        self.assertEqual(sorted(result), [4, 5])

    def test_is_prime_true(self):
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(3))
        self.assertTrue(is_prime(11))

    def test_is_prime_false(self):
        self.assertFalse(is_prime(1))
        self.assertFalse(is_prime(4))
        self.assertFalse(is_prime(15))

    def test_generate_pascals_triangle(self):
        expected_output = [
            [1],
            [1, 1],
            [1, 2, 1],
            [1, 3, 3, 1],
            [1, 4, 6, 4, 1],
        ]
        self.assertEqual(generate_pascals_triangle(5), expected_output)

    def test_generate_pascals_triangle_zero_rows(self):
        self.assertEqual(generate_pascals_triangle(0), [])

    def test_generate_pascals_triangle_one_row(self):
        self.assertEqual(generate_pascals_triangle(1), [[1]])

    def test_generate_star_pattern(self):
        expected_output = "*\n**\n***\n****\n*****"
        self.assertEqual(generate_star_pattern(5), expected_output)

    def test_generate_number_pattern(self):
        expected_output = "1\n2 2\n3 3 3\n4 4 4 4\n5 5 5 5 5"
        self.assertEqual(generate_number_pattern(5), expected_output)

    def test_generate_diamond_pattern(self):
        expected_output = "  *\n ***\n*****\n ***\n  *"
        self.assertEqual(generate_diamond_pattern(5), expected_output)

    def test_is_palindrome_simple(self):
        self.assertTrue(is_palindrome("racecar"))

    def test_is_palindrome_with_spaces(self):
        self.assertTrue(is_palindrome("A man, a plan, a canal, Panama!"))

    def test_is_palindrome_false(self):
        self.assertFalse(is_palindrome("hello"))

    def test_merge_sorted_lists(self):
        list1 = [1, 3, 5]
        list2 = [2, 4, 6]
        result = merge_sorted_lists(list1, list2)
        self.assertEqual(result, [1, 2, 3, 4, 5, 6])

    def test_merge_sorted_lists_empty(self):
        list1 = []
        list2 = [1, 2, 3]
        result = merge_sorted_lists(list1, list2)
        self.assertEqual(result, [1, 2, 3])

    def test_count_vowels(self):
        self.assertEqual(count_vowels("hello"), 2)
        self.assertEqual(count_vowels("HELLO"), 2)
        self.assertEqual(count_vowels("Python Programming"), 4)

    def test_fibonacci_sequence(self):
        self.assertEqual(fibonacci_sequence(10), [0, 1, 1, 2, 3, 5, 8])
        self.assertEqual(fibonacci_sequence(1), [0])

    def test_fibonacci_sequence_zero(self):
        self.assertEqual(fibonacci_sequence(0), [])

    def test_validate_password_valid(self):
        self.assertTrue(validate_password("StrongPass1!"))
        self.assertTrue(validate_password("AnotherGoodOne123@"))

    def test_validate_password_invalid(self):
        self.assertFalse(validate_password("weak"))
        self.assertFalse(validate_password("NoSpecialChar123"))
        self.assertFalse(validate_password("Short1!"))

    def test_collect_numbers(self):
        # Mock input to simulate entering numbers and 'done'
        with unittest.mock.patch('builtins.input', side_effect=["10", "20", "done"]):
            with unittest.mock.patch('builtins.print') as mock_print:
                collect_numbers()
                mock_print.assert_called_with("Sum: 30.0, Average: 15.0")

    def test_collect_numbers_invalid_input(self):
        # Mock input to simulate invalid input followed by valid input
        with unittest.mock.patch('builtins.input', side_effect=["abc", "10", "done"]):
            with unittest.mock.patch('builtins.print') as mock_print:
                collect_numbers()
                mock_print.assert_called_with("Sum: 10.0, Average: 10.0")

    def test_menu_system_add_student(self):
        # Mock input to simulate adding a student
        with unittest.mock.patch('builtins.input', side_effect=["1", "John", "25", "3"]):
            with unittest.mock.patch('builtins.print') as mock_print:
                menu_system()
                mock_print.assert_any_call("Student John added successfully.")

    def test_menu_system_display_students(self):
        # Mock input to simulate displaying students
        with unittest.mock.patch('builtins.input', side_effect=["1", "Jane", "22", "2", "3"]):
            with unittest.mock.patch('builtins.print') as mock_print:
                menu_system()
                mock_print.assert_any_call("Name: Jane, Age: 22, Average Grade: 0.00")


if __name__ == "__main__":
    unittest.main()