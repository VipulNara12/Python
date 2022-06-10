# print multiplication of Given number
'''t = int(input("Enter the number for multiplication\n"))
i=0
for i in range(1,11):
  
  print(f"{t}*{i}={t*i}")
  i = i+1 '''
  

# Greet all the person in list with the name start with given number

'''l1 = ["Harry", "Shyam", "Sachin", "Rahul"]

for name in l1:
    if name.startswith("S"):
        print("Good Morning", name) '''


# print multiplication of Given number using while loop

''' t = int(input("Enter the number for multiplication\n"))
i=1
while i < 11:
    print(f"{t}*{i}={t*i}")
    i = i+1'''

# find a given number is prime or not

'''from ast import Break


num = int(input("Enter a number\n"))
prime = True
for i in range(2, num):
    if (num%i==0):
        prime = False
        Break
if prime:        
    print("Entered number is prime number.")    
else: 
    print("Entered number is not prime number.")    '''

num=[1,2,3,4]
n= len(num)
print(type(num))
print(n)
print("sum of array",n*(n+1)/2)