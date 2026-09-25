m1 = int(input("Enter mark 1: "))
m2 = int(input("Enter mark 2: "))
m3 = int(input("Enter mark 3: "))

total = m1 + m2 + m3
average = total / 3
percentage = (total / 300) * 100
remaining = 300 - total

print("Total =", total)
print("Average =", average)
print("Percentage =", percentage, "%")
print("Remaining Marks =", remaining)
