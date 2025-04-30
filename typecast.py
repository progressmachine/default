# Explicit Typecasting

name = "Pranish"
age = 18
gpa = 3.8
student = True

print(type(name))
print(type(age))
print(type(gpa))
print(type(student))

print(age)
age = float(age)
print(type(age))
print(age)

print(gpa)
gpa = int(gpa)
print(type(gpa))
print(gpa)

print(student)
student = str(student)
print(type(student))
print(student)

age = bool(age) # If a number is anything but 0, then converting it into boolean makes it True.
print(age)

# If a string is anything but empty, then converting it into boolean makes it True.
empty = ""
not_empty = " "
print(empty)
empty = bool(empty)
print(empty)
print(not_empty)
not_empty = bool(not_empty)
print(not_empty)

# Implicit Typecasting

x = 1
y = 4
x = x/y
print(x)
print(type(x))

l = 2
m = 2.0
l = l/m
print(l)
print(type(l))
