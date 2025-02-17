from flask import Flask, request, render_template

app = Flask(__name__)

class Employee:
    employee_ids = set()  
    
    def __init__(self, employee_id, name, department):
        if employee_id in Employee.employee_ids:
            raise ValueError("Employee ID must be unique.")
        
        self.employee_id = employee_id
        self.name = name
        self.department = department
        Employee.employee_ids.add(employee_id)

    def display_employee(self):
        return f"Employee ID: {self.employee_id}, Name: {self.name}, Department: {self.department}"


employees = {}

@app.route('/')
def home():
    return render_template('home.html')  

@app.route('/add_employee', methods=['GET', 'POST'])
def add_employee():
    if request.method == 'POST':
        try:
            employee_id = request.form['employee_id']
            name = request.form['name']
            department = request.form['department']

            if not all([employee_id, name, department]):
                return "Missing parameters. Please provide employee_id, name, and department.", 400

            if employee_id in employees:
                return "Employee ID already exists.", 400

            employee = Employee(employee_id, name, department)
            employees[employee_id] = employee

            return f"Employee added successfully: {employee.display_employee()}"
        except ValueError as e:
            return str(e), 400
    return render_template('add_employee.html')

if __name__ == '__main__':
    app.run(debug=True)
