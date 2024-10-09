def read_employees(csv_file_location):
    """Reads the CSV file and returns a list of dictionaries representing the employees."""
    with open(csv_file_location, mode='r') as file:
        csv_reader = csv.DictReader(file)
        employee_list = [row for row in csv_reader]
        # Print the keys of the first row to check the column names
        if employee_list:
            print("Column names:", employee_list[0].keys())
    return employee_list

def process_data(employee_list):
    """Counts the number of employees in each department."""
    department_count = {}
    for employee in employee_list:
        department = employee['Department']  # Use the correct column name
        if department not in department_count:
            department_count[department] = 1
        else:
            department_count[department] += 1
    return department_count

def write_report(department_count, report_file):
    """Writes the department count report to a plain text file."""
    with open(report_file, mode='w') as file:
        for department, count in department_count.items():
            file.write(f"{department}: {count}\n")

# File locations
csv_file_location = '../data/employees.csv'
report_file = 'department_report.txt'

# Read the employee data
employee_list = read_employees(csv_file_location)

# Process the data to get the department counts
department_count = process_data(employee_list)

# Write the report to a file
write_report(department_count, report_file)

print("Report generated successfully!")