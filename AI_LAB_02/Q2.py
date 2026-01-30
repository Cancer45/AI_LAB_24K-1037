class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id

    def calculate_salary(self):
        pass

class FullTimeEmployee(Employee):
    def __init__(self, name, emp_id, monthly_salary):
        super().__init__(name, emp_id)
        self.monthly_salary = monthly_salary

    def calculate_salary(self):
        return self.monthly_salary

class PartTimeEmployee(Employee):
    def __init__(self, name, emp_id, hours_worked, hourly_rate):
        super().__init__(name, emp_id)
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate

    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked

ft_employee = FullTimeEmployee("Hakim", 1034, 90000)
pt_employee = PartTimeEmployee("Usman", 3341, 72, 540)

print("salary (Full Time): ", ft_employee.calculate_salary())
print("salary (Part Time): ", pt_employee.calculate_salary())
