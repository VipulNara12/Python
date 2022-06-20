
max = int(input("Enter the max number\n"))

odd_num= []

for i in range(1,max):
    if i % 2 ==1:
        odd_num.append(i)

print("Odd Numbers: ", odd_num)