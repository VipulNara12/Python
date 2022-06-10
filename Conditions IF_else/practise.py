'''username = input("Enter the username\n")

if len(username) > 10:
    print("Entered Username is contain more than 10 Characters.")
else:
    print("Username is not contain more than 10 Characters.")




name_list = ["Rahul", "Jatin", "Sachin", "Sonu"]

name= input("Enter the Name\n")

if name in name_list:
    print("Entered name present in List")
else:
    print("Entered name is not present in List")   '''

from joblib import PrintTime


marks = int(input("Enter the Marks\n"))

if marks >=90:
    print("Excellent")
elif marks >=80 and marks <=90:
    print("A")
elif marks >=70 and marks <=80:
    print("B")
elif marks >=60 and marks <=70:
    print("C")
elif marks >=50 and marks <=60:
    print("D")
else:
    print("E")