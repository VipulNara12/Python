class Employee:
    company= "Google"
    salary = 59000
    salBonus = 5000

    @property 
    def totalSalary(self):
        return self.salary + self.salBonus

    @totalSalary.setter
    def totalSalary(self, val):
        self.salBonus = val - self.salary


e = Employee()
print(e.totalSalary)
e.totalSalary = 62000
print(e.salary)
print(e.salBonus)
