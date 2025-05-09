# Exploring the 'range()' function in Python

# 1. Basic use of range: from 0 to 4 (5 is not included)
print("1. Counting from 0 to 4:")
for i in range(5):
    print(i)
print()

# 2. Range with a start and end value
print("2. Counting from 2 to 6:")
for i in range(2, 7):  # Starts at 2, ends at 6 (7 is not included)
    print(i)
print()

# 3. Range with a step value
print("3. Counting from 0 to 10 in steps of 2:")
for i in range(0, 11, 2):  # Start at 0, go up to 10, step by 2
    print(i)
print()

# 4. Counting backward using a negative step
print("4. Counting down from 5 to 1:")
for i in range(5, 0, -1):  # Start at 5, stop just before 0, step down by 1
    print(i)
print()

# 5. Using range with len() to loop through list indices
fruits = ['apple', 'banana', 'cherry']
print("5. Looping through a list using range and len():")
for i in range(len(fruits)):
    print(f"Index {i}: {fruits[i]}")
print()

# 6. Creating a list from a range using list()
print("6. Creating a list from range(1, 6):")
numbers = list(range(1, 6))
print(numbers)
print()

# 7. Using range in a while loop (advanced)
print("7. Using range manually in a while loop:")
r = range(3)
i = 0
while i < len(r):
    print(f"r[{i}] = {r[i]}")
    i += 1