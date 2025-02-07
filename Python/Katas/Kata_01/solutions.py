# todo.py

def add_two_numbers(a, b):
    """
    Add two numbers and return their sum.
    """
    return a + b


def reverse_string(s):
    """
    Reverse a given string and return the reversed version.
    """
    return s[::-1]


def find_largest_number(numbers):
    """
    Find and return the largest number in a list of integers.
    """
    largest_num = numbers[0]
    for number in numbers:
        if number >= largest_num:
            largest_num = number
    return largest_num


def count_vowels(s):
    """
    Count and return the number of vowels in a given string.
    """
    vowels = "aeiou"
    counter = 0
    for character in s:
        if character.lower() in vowels:
            counter += 1
    return counter


def fibonacci_sequence(n):
    """
    Generate and return the first n numbers in the Fibonacci sequence.
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    
