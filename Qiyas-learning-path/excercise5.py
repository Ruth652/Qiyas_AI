from functools import reduce
# =====================================================
# Exercise 5: University Course Registration System
# =====================================================

courses = [
    ("Math", 45),
    ("Physics", 60),
    ("Biology", 25),
    ("Chemistry", 75),
    ("History", 30)
]


def highest_enrollment(course_list):
    """
    Return course with highest enrollment.
    """
     
    return reduce(lambda acc, c: max(acc, c[1]), course_list, 0)


def low_enrollment_courses(course_list):
    """
    Return courses with enrollment below 40.
    """
    return reduce(lambda acc, c : min(acc, c[1]), course_list, 0)
    


def total_registered_students(course_list):
    """
    Calculate total registered students.
    """
    return reduce(lambda acc, c: acc + c[1], course_list, 0)


def add_extra_students(course_list):
    """
    Add 5 extra students using map().
    """
    return list(map(lambda c: (c[0] + c[1])))


def sort_courses(course_list):
    """
    Sort courses by enrollment.
    """
    pass


def process_enrollments(course_list):
    """
    Square even enrollments.
    Cube odd enrollments.
    """
    pass


def popular_courses(course_list):
    """
    Use filter() to get courses above 50 students.
    """
    pass