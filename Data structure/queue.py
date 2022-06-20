
queue_sample = []
def enqueue():
    element = int(input("Enter the Elements"))
    queue_sample.append(element)
    print(element," is added into queue.")
def dequeue():
    if not queue_sample:
        print("Queue is Empty.")
    else:
        d = queue_sample.pop(0)
        print("Removed element: ", d)
def show():
    print(queue_sample)

while True:
    print("Enter the choice 1. Enqueue 2. Dequeue 3. Show Queue 4. Quit")
    choice= int(input())
    if choice == 1:
        enqueue()
    elif choice == 2:
        dequeue()
    elif choice == 3:
        show()
    elif choice == 4:
        break
    else:
        print("Enter the Correct operation.")