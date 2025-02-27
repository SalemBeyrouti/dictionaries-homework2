company_employees = {}

departments = int(input("Enter number of departments: "))

for i in range (departments):

    department_name = input("Enter the name of the department: ")

    company_employees[department_name] = {}

    num_employees = int(input(f"Enter the number of employees in {department_name} department: "))

    for j in range(num_employees):
        employee_name = input("Enter the name of the employee: ")
        employee_age = int(input(f"Enter the age of {employee_name}: "))
        employee_role = input(f"Enter role of {employee_name}: ")
# thought it was more clear to impliment f inside input 
        company_employees[department_name][employee_age] = {"age": employee_age, "role": employee_role}


print (company_employees)