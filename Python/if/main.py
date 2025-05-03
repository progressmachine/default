age = int(input("Enter your age: "))

if age > 999:
    print("You are too old to sign up.")
elif age >= 18:
    print("You have been signed up.")
elif age < 0:
    print("You haven't been born yet.")
else:
    print("You must be 18+ to sign up.")