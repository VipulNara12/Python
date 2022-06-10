class A:

    def __init__(self):
        print("Init of A")

    def feature1(self):
        print("Feature 1 is working")

    def feautre2(self):
        print("Feature 2 is working")

class B():

    def __init__(self):
        print("Init of B")

    def feature3(self):
        print("Feature 3 is working")

    def feautre4(self):
        print("Feature 4 is working")

class C(A,B): 

    def __init__(self):
        super().__init__()  # super() method calls class A Init() because of Method Resolution Order(MRO)
        print("Init of C")
    def feature5(self):
        super().feature1() # we can also call function using super()

a1 = C()

a1.feature5()