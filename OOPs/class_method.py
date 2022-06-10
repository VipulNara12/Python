class Employee:

    company = "Google"
    salary = 100
    location = "Delhi"

    @classmethod
    def changeSalary(cls, sal):
        cls.salary = 500

e = Employee()
print(e.salary)
e.changeSalary(500)
print(e.salary)