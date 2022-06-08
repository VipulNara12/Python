def percentage(marks):
    return sum(marks)/(n*100)*100

mark1 = [78,73,54,87,89]
n= len(mark1)
percentage1= percentage(mark1)

mark2 = [85,68,95,65]
n= len(mark2)
percentage2= percentage(mark2)
print(percentage1, percentage2)
