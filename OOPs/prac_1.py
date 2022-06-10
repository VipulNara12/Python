


class Programmer:
    company = "Microsoft"

    def __init__(self, name, product):
        self.name = name
        self.product = product

    def getInfo(self):
        print(f"Name of {self.company} Programmer is {self.name} & Name of Product is {self.product}")

harry = Programmer("Harry", "Skype")
alka = Programmer("Alka", "Github")
harry.getInfo()
alka.getInfo()

