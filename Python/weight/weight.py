weight = float(input("Enter your weight: "))
unit = input("Kilograms or Pounds? (K / L): ")

if unit.capitalize() == "K":
    weight *= 2.205
elif unit.capitalize() == "L":
    weight /= 2.205
else:
    print(f"{unit} is not a valid unit.")

# used ternary operators below
print(f"Your weight is {round(weight,2)} {"kilograms" if unit.capitalize == "K" else "pounds"}.")