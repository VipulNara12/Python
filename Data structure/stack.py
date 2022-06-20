from secrets import choice


stack = []
def push():
    element = int(input("Enter the Elements\n"))
    stack.append(element)
    print(stack)

def popElement():
    if not stack:
        print("Stack is empty")
    else:
        p = stack.pop()
        print("Removed element: ", p)
        print(stack)
    
while True:
    print("Select the Operation 1. Push, 2. Pop 3. Exit")
    choice = int(input())
    if choice == 1:
        push()
    elif choice == 2:
        popElement()
    elif choice == 3:
        break    
    else:
        print("Enter the correct operation")





'''
stack = []
stack.append(5)
stack.append(10)
stack.append(15)
#stack.pop()
#stack.pop()
#stack.pop()
print(stack)

# Indexing
print(stack[1])

# To check whether stack is empty or not.
if(len(stack)==0):
    print("Empty")
else:
    print("not empty")
'''