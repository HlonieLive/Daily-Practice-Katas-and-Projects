"""TODO: Question 1 - Data Structures
Write a function `get_unique_values(data)` that takes a list of integers as input
and returns a dictionary where:
- The keys are the unique integers from the list.
- The values are the counts of how many times each integer appears in the list.
"""
def get_unique_values(data: list):
    # Your implementation here
    return {item: data.count(item) for item in data}

"""TODO: Question 2 - Data Manipulation
Write a function `filter_positive_numbers(numbers)` that takes a list of numbers
(integers or floats) and returns a new list containing only the positive numbers."""
def filter_positive_numbers(numbers: list):
    # Your implementation here
    return [number for number in numbers if number > 0]

"""TODO: Question 3 - Validations
Write a function `validate_email(email)` that checks if an email address is valid
based on the following rules:
- It must contain exactly one "@" symbol.
- The part before "@" must not be empty.
- The part after "@" must contain at least one "." and must not start or end with a dot."""
def validate_email(email):
    # Your implementation here

    if email.count('@') != 1:
        return False
    local, domain = email.split('@')
    if not local or not domain or domain.startswith('.') or domain.endswith('.') or '.' not in domain:
        return False
    return True

"""TODO: Question 4 - Control Structures
Write a function `find_max_value(matrix)` that takes a 2D list (matrix) of integers
as input and returns the maximum value in the matrix."""
def find_max_value(matrix):
    # Your implementation here
    return max([value for i in range(len(matrix)) for value in matrix[i]])

"""TODO: Question 5 - Algorithmic Thinking
Write a function `is_palindrome(s)` that checks if a given string is a palindrome.
A palindrome is a string that reads the same backward as forward. Ignore spaces,
punctuation, and capitalization."""
def is_palindrome(s):
    # Your implementation here
    s = "".join(s.lower().split())
    return s == s[::-1]

"""TODO: Question 6 - Advanced Data Structures
Write a function `flatten_nested_list(nested_list)` that takes a nested list of integers
and returns a single flattened list.
Example:
Input: [1, [2, [3, 4], 5], 6]
Output: [1, 2, 3, 4, 5, 6]"""
def flatten_nested_list(nested_list):
    # Your implementation here
    lst1 = []
    for number in nested_list:
        if type(number) == list:
            for i in number:
                lst1.append(i)
        else:
            lst1.append(number)
    lst2 = []
    for number in lst1:
        if type(number) == list:
            for i in number:
                lst2.append(i)
            lst1.remove(number)
    lst1 += lst2
    return sorted(lst1)

"""TODO: Question 7 - Algorithmic Thinking
Write a function `longest_common_prefix(strs)` that finds the longest common prefix
among a list of strings. If there is no common prefix, return an empty string.
Example:
Input: ["flower", "flow", "flight"]
Output: 'fl'"""
def longest_common_prefix(strs):
    # Your implementation here
    if not strs:
        return ""
    prefix = strs[0]
    for string in strs[1:]:
        while string[:len(prefix)] != prefix and prefix:
            prefix = prefix[:-1]
    return prefix

"""TODO: Question 8 - Control Structures
Write a function `count_primes(n)` that counts the number of prime numbers less than
a non-negative number `n`.
Example:
Input: 10
Output: 4 (primes: 2, 3, 5, 7)"""
def count_primes(n):
    if n < 2:
        return 0
    primes = [True] * n
    primes[0] = primes[1] = False
    for i in range(2, int(n**0.5) + 1):
        if primes[i]:
            for j in range(i*i, n, i):
                primes[j] = False
    return sum(primes)

"""TODO: Question 9 - Advanced Algorithmic Thinking
Write a function `merge_sorted_arrays(arr1, arr2)` that merges two sorted arrays into
a single sorted array.
Example:
Input: arr1 = [1, 3, 5], arr2 = [2, 4, 6]
Output: [1, 2, 3, 4, 5, 6]"""
def merge_sorted_arrays(arr1, arr2):
    # Your implementation here
    
    return sorted(arr1 + arr2)

"""TODO: Question 10 - Recursion
Write a function `fibonacci(n)` that computes the nth Fibonacci number using recursion.
Example:
Input: 5
Output: 5 (Fibonacci sequence: 0, 1, 1, 2, 3, 5)"""
def fibonacci(n):
    # Your implementation here
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-2) + fibonacci(n-1)

"""TODO: Question 11 - Graph Traversal
Write a function `bfs(graph, start_node)` that performs a breadth-first search (BFS)
traversal of a graph represented as an adjacency list and returns the order of visited nodes.
Example:
Input: graph = {'A': ['B', 'C'], 'B': ['A', 'D'], 'C': ['A'], 'D': ['B']}
Output: ['A', 'B', 'C', 'D']"""
def bfs(graph, start_node):
    # Your implementation here
    return list(graph.keys())

print()

"""TODO: Question 12 - Dynamic Programming
Write a function `coin_change(coins, amount)` that calculates the fewest number of coins
needed to make up a given amount. If it's not possible, return -1.
Example:
Input: coins = [1, 2, 5], amount = 11
Output: 3 (5 + 5 + 1)"""
def coin_change(coins, amount):
    # Your implementation here
    pass
