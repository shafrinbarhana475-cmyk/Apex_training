students = ["Arun", "Bala", "Kavin", "Ravi"]

print("Original Students =", students)

# 1. append()
students.append("Vijay")
print("After append =", students)

# 2. extend()
students.extend(["Hari", "Ajay"])
print("After extend =", students)

# 3. insert()
students.insert(1, "Rahul")
print("After insert =", students)

# 4. remove()
students.remove("Bala")
print("After remove =", students)

# 5. pop()
students.pop()
print("After pop =", students)

# 6. index()
print("Index of Kavin =", students.index("Kavin"))

# 7. count()
print("Count of Kavin =", students.count("Kavin"))

# 8. sort()
students.sort()
print("After sort =", students)

# 9. reverse()
students.reverse()
print("After reverse =", students)

# 10. copy()
student_copy = students.copy()
print("Copied Students =", student_copy)

# 11. clear()
temp_students = students.copy()
temp_students.clear()
print("After clear =", temp_students)

# 12. sum(), min(), max(), len()
marks = [85, 72, 90, 68]

print("Marks =", marks)
print("Total Marks =", sum(marks))
print("Minimum Mark =", min(marks))
print("Maximum Mark =", max(marks))
print("Number of Marks =", len(marks))
