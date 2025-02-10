
def add_student(students: dict,  name: str, student_id: str, grade: list[int, int, int])-> str:
    """Adds a new student to the dictionary"""

    if student_id in students.keys():
        raise ValueError()
     
    students[student_id] = {"name": name, "grade": grade}
    return students

def calculate_average(students: dict, student_id: str) -> float:
    """Computes the average grade of a student"""
    


def has_passed(students: dict, student_id: str)-> bool:
    """Checks is a student passed based on their average grade"""
    pass 

