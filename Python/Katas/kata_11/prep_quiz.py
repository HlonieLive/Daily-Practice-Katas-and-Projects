# TODO 1: Define a class `Student` with attributes `name`, `age`, and `grades`.
#         Include methods to:
#         - Add grades (ensure grades are between 0 and 100).
#         - Calculate the average grade.
#         - Display student information (name, age, and average grade).

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.grades = []

    def add_grades(self, grade):
        if grade not in range(101):
            raise ValueError("Grades can't be negative or greater than 100!")
                    
        return self.grades.append(grade)
    
    def calculate_average(self):
        if self.grades == []:
            return "The are no Grades available!"
        return sum(self.grades)/len(self.grades)


# TODO 2: Create a function `get_positive_integer` that prompts the user for input until a valid positive integer is entered.
def get_positive_integer(prompt="Enter a positive integer: "):
    positive_integer = int(input(prompt))
    while positive_integer < 0:
        print("\nNumber must be greater than 0!\n")
        positive_integer = int(input(prompt))
    return f"\nThe positive integer is: {positive_integer}"

print(get_positive_integer())


# TODO 3: Implement a function `find_common_elements` that takes two lists and returns their common elements using a set.
def find_common_elements(list1, list2):
    return set([element for element in list1 if element in list2])


# TODO 4: Write a program that uses a loop to repeatedly ask the user for numbers until they type 'done'.
#         Store the numbers in a list and then calculate the sum and average.
def collect_numbers():

    numbers = []
    reply = input("Enter a number: \nType 'done' to exit!")
    while reply != "done":
        numbers.append(int(reply))
        reply = input("Enter a number: \nType 'done' to exit!")
    sum_of_num = sum(numbers)
    average = sum_of_num/len(numbers)
    
    return f"The sum of numbers is:     {sum_of_num}\nThe average of numbers is:    {average}"


# TODO 5: Create a dictionary-based menu system where the user can select options by entering a number.
#         Options include:
#         1) Add a student (prompt for name and age, then create a Student object).
#         2) Display all students (show their details using the `display_info` method).
#         3) Exit the program.
def menu_system():
    pass


# TODO 6: Implement a function `is_palindrome` that checks if a given string is a palindrome (case-insensitive).
#         Ignore non-alphanumeric characters.
def is_palindrome(s):
    pass


# TODO 7: Implement a function `merge_sorted_lists` that takes two sorted lists and merges them into a single sorted list.
#         Do not use the built-in `sort()` or `sorted()` functions.
def merge_sorted_lists(list1, list2):
    pass


# TODO 8: Implement a function `count_vowels` that counts the number of vowels (a, e, i, o, u) in a given string.
#         The function should be case-insensitive.
def count_vowels(s):
    pass


# TODO 9: Implement a function `fibonacci_sequence` that generates the Fibonacci sequence up to a given number `n`.
#         Return the sequence as a list.
def fibonacci_sequence(n):
    pass


# TODO 10: Implement a function `validate_password` that checks if a password meets the following criteria:
#          - At least 8 characters long.
#          - Contains at least one uppercase letter, one lowercase letter, one digit, and one special character.
def validate_password(password):
    pass


# TODO 11: Implement a function `generate_star_pattern` that generates a right-angled triangle pattern of stars.
#         Example: For n=5, the output should be:
#         *
#         **
#         ***
#         ****
#         *****
def generate_star_pattern(n):
    pass


# TODO 12: Implement a function `generate_number_pattern` that generates a number pyramid pattern.
#         Example: For n=5, the output should be:
#         1
#         2 2
#         3 3 3
#         4 4 4 4
#         5 5 5 5 5
def generate_number_pattern(n):
    pass


# TODO 13: Implement a function `generate_diamond_pattern` that generates a diamond pattern of stars.
#         Example: For n=5, the output should be:
#             *
#            ***
#           *****
#            ***
#             *
def generate_diamond_pattern(n):
    pass


# TODO 14: Implement a function `is_prime` that checks if a given number is a prime number.
#         A prime number is greater than 1 and divisible only by 1 and itself.
def is_prime(n):
    pass


# TODO 15: Implement a function `generate_pascals_triangle` that generates Pascal's Triangle up to `n` rows.
#         Each row in Pascal's Triangle is constructed by adding adjacent numbers from the previous row.
#         Example: For n=5, the output should be:
#         [1]
#         [1, 1]
#         [1, 2, 1]
#         [1, 3, 3, 1]
#         [1, 4, 6, 4, 1]
def generate_pascals_triangle(n):
    pass


# TODO 16: Test all the above functionalities by calling the appropriate functions.
if __name__ == "__main__":
    pass
