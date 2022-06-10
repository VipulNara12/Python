# Example of Single Inheritance
'''
class A:

    def feature1(self):
        print("Feature 1 is working")

    def feautre2(self):
        print("Feature 2 is working")

class B(A):

    def feature3(self):
        print("Feature 3 is working")

    def feautre4(self):
        print("Feature 4 is working")


a1 = B()

a1.feature1()'''

# Example of Multilevel Inheritance
'''
class A:

    def feature1(self):
        print("Feature 1 is working")

    def feautre2(self):
        print("Feature 2 is working")

class B(A):

    def feature3(self):
        print("Feature 3 is working")

    def feautre4(self):
        print("Feature 4 is working")

class C(B):

    def feature5(self):
        print("Feature 5 is working")

a1 = C()

a1.feature1()
'''

# Example of Multiple Inheritance
'''
class A:

    def feature1(self):
        print("Feature 1 is working")

    def feautre2(self):
        print("Feature 2 is working")

class B():

    def feature3(self):
        print("Feature 3 is working")

    def feautre4(self):
        print("Feature 4 is working")

class C(A,B):

    def feature5(self):
        print("Feature 5 is working")

a1 = C()

a1.feature1()

'''


    