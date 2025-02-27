company_employees = {}

departments = int(input("Enter number of departments: "))

for i in range (departments):

    department_name = input("Enter the name of the department: ")

    company_employees[department_name] = {}

print (company_employees)