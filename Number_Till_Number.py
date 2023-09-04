number=int(input("Enter a number"))
print("This is the sum of all the numbers before", number, ":")
total=0
for i in range(0, number, 1):
    total=total+i

print("The sum of all the numbers before", number,"is", total)
