import unittest
from practice_quize import *


class TestStudentClass(unittest.TestCase):
    def test_student_initialization(self):
        student = Student("Alice", 20)
        self.assertEqual(student.name, "Alice")
        self.assertEqual(student.age, 20)
        self.assertEqual(student.grades, [])


class TestGetPositiveInteger(unittest.TestCase):
    def test_get_positive_integer_valid(self):
        with unittest.mock.patch('builtins.input', return_value="42"):
            result = get_positive_integer()
            self.assertEqual(result, 42)


class TestFindCommonElements(unittest.TestCase):
    def test_find_common_elements(self):
        list1 = [1, 2, 3, 4, 5]
        list2 = [4, 5, 6, 7, 8]
        result = find_common_elements(list1, list2)
        self.assertEqual(sorted(result), [4, 5])


class TestIsPrime(unittest.TestCase):
    def test_is_prime_true(self):
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(3))
        self.assertTrue(is_prime(11))

    def test_is_prime_false(self):
        self.assertFalse(is_prime(1))
        self.assertFalse(is_prime(4))
        self.assertFalse(is_prime(15))


class TestGeneratePascalsTriangle(unittest.TestCase):
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


class TestGenerateStarPattern(unittest.TestCase):
    def test_generate_star_pattern(self):
        expected_output = "*\n**\n***\n****\n*****"
        self.assertEqual(generate_star_pattern(5), expected_output)


class TestGenerateNumberPattern(unittest.TestCase):
    def test_generate_number_pattern(self):
        expected_output = "1\n2 2\n3 3 3\n4 4 4 4\n5 5 5 5 5"
        self.assertEqual(generate_number_pattern(5), expected_output)


class TestGenerateDiamondPattern(unittest.TestCase):
    def test_generate_diamond_pattern(self):
        expected_output = "  *\n ***\n*****\n ***\n  *"
        self.assertEqual(generate_diamond_pattern(5), expected_output)


class TestIsPalindrome(unittest.TestCase):
    def test_is_palindrome_simple(self):
        self.assertTrue(is_palindrome("racecar"))

    def test_is_palindrome_with_spaces(self):
        self.assertTrue(is_palindrome("A man, a plan, a canal, Panama!"))

    def test_is_palindrome_false(self):
        self.assertFalse(is_palindrome("hello"))


class TestMergeSortedLists(unittest.TestCase):
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


class TestCountVowels(unittest.TestCase):
    def test_count_vowels(self):
        self.assertEqual(count_vowels("hello"), 2)
        self.assertEqual(count_vowels("HELLO"), 2)
        self.assertEqual(count_vowels("Python Programming"), 4)


class TestFibonacciSequence(unittest.TestCase):
    def test_fibonacci_sequence(self):
        self.assertEqual(fibonacci_sequence(10), [0, 1, 1, 2, 3, 5, 8])
        self.assertEqual(fibonacci_sequence(1), [0])

    def test_fibonacci_sequence_zero(self):
        self.assertEqual(fibonacci_sequence(0), [])


class TestValidatePassword(unittest.TestCase):
    def test_validate_password_valid(self):
        self.assertTrue(validate_password("StrongPass1!"))
        self.assertTrue(validate_password("AnotherGoodOne123@"))

    def test_validate_password_invalid(self):
        self.assertFalse(validate_password("weak"))
        self.assertFalse(validate_password("NoSpecialChar123"))
        self.assertFalse(validate_password("Short1!"))


if __name__ == "__main__":
    unittest.main()