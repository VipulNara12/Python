'''class computer:

    def __init__(self):
        print("hello")

    def config(self):
        print("i5, 16gb, 1TB")

comp1 = computer()
comp2 = computer()

computer.config(comp1)
computer.config(comp2)    


comp1.config()
comp2.config() '''

class computer:

    def __init__(self, cpu, ram):
        self.cpu = cpu
        self.ram = ram

    def config(self):
        print(f"Config is: CPU {self.cpu} RAM {self.ram}")

comp1 = computer('i5', '16GB')
comp2 = computer('Ryzen 3', '8GB')

comp1.config()
comp2.config()