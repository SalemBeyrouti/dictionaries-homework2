company_employees = {}

departments = int(input("Enter number of departments: "))

for i in range (departments):

    department_name = input("Enter the name of the department: ")

    company_employees[department_name] = {}

    num_employees = int(input("Enter the number of employees in department: "))

    for j in range(num_employees):
        employee_name = input("Enter the name of the employee: ")
        employee_age = int(input("Enter the age of the employee: "))
        employee_role = input("Enter role of employee: ")

        company_employees[department_name][employee_age] = {"age": employee_age, "role": employee_role}


print (company_employees)