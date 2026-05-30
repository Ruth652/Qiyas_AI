# =====================================================
# Exercise 2: Employee Salary Management System
# =====================================================

employees = [
    ("John", "Developer", 5000),
    ("Sara", "Manager", 8000),
    ("Mike", "Designer", 4500),
    ("Helen", "Developer", 6500),
    ("David", "Manager", 7200)
]


def highest_paid_employee(employee_list):
    return max(e[2] for e in employee_list)


def average_salary(employee_list):
    return sum(e[2] for e in employee_list) / len(employee_list)
  


def employees_above_average(employee_list):
    avg = average_salary(employee_list)
    return list(filter(lambda e: e[2] > avg, employee_list ))
    


def add_salary_bonus(employee_list):
    return list(map(lambda e: (e[0], e[1], e[2] + 10), employee_list))



def sort_by_salary(employee_list):
    e = sorted(employee_list, key=lambda e: e[2])
    return e

#   students.sort(key=lambda student: student[1], reverse=True)
def double_low_salaries(employee_list):
    """
    Create a list with doubled salaries
    for salaries below 6000.
    """
    e_blow = list(filter(lambda e: e[2] < 6000, employee_list))
    
    return list(map(lambda e:(e[0], e[1], e[2] * 2), e_blow))
   
   


def developers_only(employee_list):
    """
    Use filter() to return only developers.
    """
    return list(filter(lambda e: e[1] == "Developer", employee_list))
    


print("highest",highest_paid_employee(employees))
print("average_salary",average_salary(employees))
print("employees_above_average",employees_above_average(employees))
print("add_salary_bonus",add_salary_bonus(employees))
print("sort_by_salary",sort_by_salary(employees))
print("double_low_salaries",double_low_salaries(employees))
print("developers_only",developers_only(employees))