company_employees = {}

#for the 2nd part i have to ensure that "Engineering" is always a department

company_employees["Engineering"] = {}


departments = int(input("Enter number of departments: "))

for i in range (departments):

    department_name = input("Enter the name of the department: ")
    if department_name not in company_employees:
    
     company_employees[department_name] = {}

    num_employees = int(input(f"Enter the number of employees in {department_name} department: "))

    for j in range(num_employees):
        employee_name = input("Enter the name of the employee: ")
        employee_age = int(input(f"Enter the age of {employee_name}: "))
        employee_role = input(f"Enter role of {employee_name}: ")
# thought it was more clear to impliment f inside input 
        company_employees[department_name][employee_name] = {"age": employee_age, "role": employee_role}


# print (company_employees)

#2nd part of the exercise

company_employees["Engineering"]["David"] = {"age": 27, "role": "Data Scientist"}

print (company_employees)