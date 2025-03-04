# mock_test.py


# TODO 1: Implement a function to reverse a string using recursion.
def reverse_string_recursive(input_str):
    """
    Reverse the given string using recursion.
    :param input_str: str - The string to reverse.
    :return: str - The reversed string.
    """
    # Your implementation here
    if len(input_str) == 0:
        return input_str
    else:
        return reverse_string_recursive(input_str[1:]) + input_str[0]


# TODO 2: Create a class that implements a stack data structure using a list.
class Stack:
    """
    A simple stack implementation using a list.
    """

    def __init__(self):
        """
        Initialize an empty stack.
        """
        # Your implementation here
        pass

    def push(self, item):
        """
        Add an item to the top of the stack.
        :param item: Any - The item to add.
        """
        # Your implementation here
        pass

    def pop(self):
        """
        Remove and return the top item from the stack.
        :return: Any - The top item.
        """
        # Your implementation here
        pass

    def peek(self):
        """
        Return the top item without removing it.
        :return: Any - The top item.
        """
        # Your implementation here
        pass

    def is_empty(self):
        """
        Check if the stack is empty.
        :return: bool - True if empty, False otherwise.
        """
        # Your implementation here
        pass


# TODO 3: Write a function to check if a number is prime.
def is_prime(number):
    """
    Check if a given number is prime.
    :param number: int - The number to check.
    :return: bool - True if prime, False otherwise.
    """
    # Your implementation here
    prime_numbers = []
    
    for num in range(2, number+1):
        holder = []
        for divider in range(1, number+1):
            if num%divider == 0:
                holder.append(num)
        if len(holder) == 2:
            prime_numbers.append(num)
    print(prime_numbers)
    if number in prime_numbers:
        return True
    return False


# TODO 4: Implement a function to calculate the factorial of a number using iteration.
def factorial_iterative(n):
    """
    Calculate the factorial of a number using iteration.
    :param n: int - The number to calculate the factorial of.
    :return: int - The factorial of the number.
    """
    # Your implementation here
    if not isinstance(n, int):
        raise ValueError()
    
    if n == 0:
        return 1
    else:
        return n*(factorial_iterative(n-1))
        


# TODO 5: Write a function to process user input and validate it as an integer.
def get_user_input():
    """
    Prompt the user for input and validate it as an integer.
    :return: int - The validated integer input.
    """
    # Your implementation here
    num = int(input("Enter an integer: "))
    if not isinstance(num, int):
        raise ValueError()
    return num


# TODO 6: Generate Pascal's Triangle up to a given number of rows.
def generate_pascals_triangle(num_rows):
    """
    Generate Pascal's Triangle up to the specified number of rows.
    :param num_rows: int - The number of rows to generate.
    :return: List[List[int]] - The Pascal's Triangle as a list of lists.
    """
    # Your implementation here
    import math
    list1 = [] 
    for i in range(num_rows):
        list2 = []
        list2.append(math.comb(num_rows, i))
        list1.append(list2)
    return list2

print(generate_pascals_triangle(5))


# TODO 7: Print a right-angled triangle pattern with stars.
def print_right_angled_triangle(height):
    """
    Print a right-angled triangle pattern with stars.
    :param height: int - The height of the triangle.
    """
    # Your implementation here
    for i in range(1, height+1):
        print("*"*i)


# TODO 8: Print a pyramid pattern with stars.
def print_pyramid(height):
    """
    Print a pyramid pattern with stars.
    :param height: int - The height of the pyramid.
    """
    # Your implementation here
    for i in range(1, height+1):
        print(" "*(height-i) + "*"*(2*i-1))

# TODO 9: Print a square pattern with stars.
def print_square(side_length):
    """
    Print a square pattern with stars.
    :param side_length: int - The length of the sides of the square.
    """
    # Your implementation here
    pass
