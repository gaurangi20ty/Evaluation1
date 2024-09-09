
employees = {}


def add_employee(emp_id, name, department, salary):
    if emp_id in employees:
        print(f"Employee with ID {emp_id} already exists.")
        return
    employees[emp_id] = {
        'name': name,
        'department': department,
        'salary': salary
    }
    print(f"Employee {name} added successfully.")

def update_employee(emp_id, name=None, department=None, salary=None):
    if emp_id not in employees:
        print(f"Employee with ID {emp_id} does not exist.")
        return
    if name:
        employees[emp_id]['name'] = name
    if department:
        employees[emp_id]['department'] = department
    if salary:
        employees[emp_id]['salary'] = salary
    print(f"Employee with ID {emp_id} updated successfully.")
     
def search_employee(emp_id):
    if emp_id in employees:
        emp_details = employees[emp_id]
        print(f"Employee ID: {emp_id}")
        print(f"Name: {emp_details['name']}")
        print(f"Department: {emp_details['department']}")
        print(f"Salary: {emp_details['salary']}")
    else:
        print(f"Employee with ID {emp_id} not found.")

    

def department_wise_report():
    report = {}
    for emp_id, emp_details in employees.items():
        department = emp_details['department']
        if department not in report:
            report[department] = []
        report[department].append({
            'ID': emp_id,
            'Name': emp_details['name'],
            'Salary': emp_details['salary']
        })

   
    for department, emp_list in report.items():
        print(f"\nDepartment: {department}")
        for emp in emp_list:
            print(f"ID: {emp['ID']}, Name: {emp['Name']}, Salary: {emp['Salary']}")


add_employee(1, 'Radhikha', 'Engineering', 50000)
add_employee(2, 'Harsh', 'Marketing', 55000)
add_employee(3, 'Prateek', 'Engineering', 60000)
add_employee(4, 'Ram', 'HR', 40000)

update_employee(2, salary=58000)
search_employee(6)



department_wise_report()
