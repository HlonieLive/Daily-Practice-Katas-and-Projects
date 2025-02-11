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
    
    person["phone_number"] = phone_number
    return person

def remove_age(person):
    """Removes the age from the given person dictionary."""
    
    del person["age"]

def display_person_info(person):
    """Displays the information of the given person."""
    
    for key, value in person.items():
        print(f"{key}: {value}")

def get_keys(person):
    """Returns a list of all keys in the given person dictionary."""
    
    return [key for key in person.keys()]

def get_values(person):
    """Returns a list of all values in the given person dictionary."""
    
    return [value for value in person.values()]

def create_coordinates(x, y):
    """Creates a tuple representing coordinates."""
    
    return x, y

def append_to_list(lst, element):
    """Appends an element to the given list and returns the updated list."""
    
    lst.append(element)
    return lst

def add_to_set(s, element):
    """Adds an element to the given set and returns the updated set."""
    
    s.add(element)
    return s

def process_data(data):
    """Processes a list of tuples into a dictionary where keys are names and values are sets of ages."""
    
    dict1 = {}
    for i in range(len(data)):
        if data[i][0] not in dict1.keys():
            dict1[data[i][0]] = {data[i][1]}
        else:
            dict1[data[i][0]].add(data[i][1])
    return dict1

def get_element_at_index(lst, index):
    """Returns the element at the specified index in the list. Raises IndexError if out of bounds."""
    
    if index > len(lst):
        raise IndexError()
    return lst[index]

def double_values(lst):
    """Returns a new list with each element in the input list doubled."""
    
    return [num * 2 for num in lst]

def sum_2d_list(data):
    """Calculates the sum of all elements in a 2D list."""
    
    return sum([num for i in range(len(data)) for num in data[i]])

def find_max_2d_list(data):
    """Finds the maximum value in a 2D list."""
    pass

def unique_values_from_2d_list(data):
    """Returns a list of unique values from a 2D list."""
    pass