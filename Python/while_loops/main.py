name = input("Enter your name: ")

while name == "":
    name = input("Enter your name: ")

print(f"Hello {name}!")

age = int(input("Enter your age: "))

while age < 0:
    print("Age can't be negative.")
    age = int(input("Enter your age: "))

print(f"You are {age} years old.")

food = input("Enter a food you like (press q to quit): ")

while not food.upper() == "Q":
    print(f"You like {food}.")
    food = input("Enter another food you like (press q to quit): ")

print("Bye!")