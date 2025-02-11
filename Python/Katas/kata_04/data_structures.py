# data_structures.py

def create_person(name: str, surname: str, age: int) -> dict:
    """Creates a person dictionary with name, surname, and age."""

    return {"name" : name, "surname" : surname, "age" : age}

def update_age(person, new_age):
    """Updates the age of the given person."""
    person["age"] = new_age
    return person

def add_phone_number(person, phone_number):
    """Adds a phone number to the given person dictionary."""
    pass

def remove_age(person):
    """Removes the age from the given person dictionary."""
    pass

def display_person_info(person):
    """Displays the information of the given person."""
    pass

def get_keys(person):
    """Returns a list of all keys in the given person dictionary."""
    pass

def get_values(person):
    """Returns a list of all values in the given person dictionary."""
    pass

def create_coordinates(x, y):
    """Creates a tuple representing coordinates."""
    pass

def append_to_list(lst, element):
    """Appends an element to the given list and returns the updated list."""
    pass

def add_to_set(s, element):
    """Adds an element to the given set and returns the updated set."""
    pass

def process_data(data):
    """Processes a list of tuples into a dictionary where keys are names and values are sets of ages."""
    pass

def get_element_at_index(lst, index):
    """Returns the element at the specified index in the list. Raises IndexError if out of bounds."""
    pass

def double_values(lst):
    """Returns a new list with each element in the input list doubled."""
    pass

def sum_2d_list(data):
    """Calculates the sum of all elements in a 2D list."""
    pass

def find_max_2d_list(data):
    """Finds the maximum value in a 2D list."""
    pass

def unique_values_from_2d_list(data):
    """Returns a list of unique values from a 2D list."""
    pass