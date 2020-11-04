def avg():
    n = int(input("how many numbers:"))
    total = 0
    for i in range(n):
        x = int(input("enter any number:"))
        total += x
    average = total/n
    return average
x = avg()
print(x)