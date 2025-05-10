foods = []
prices = []
total = 0

while True:
    food = input("Enter an item (Press q to quit.): ")
    if food.lower() == "q":
        break
    price = float(input("Enter the price:  $"))
    foods.append(food)
    prices.append(price)

print()
print("You Shopping Cart!")

i = 0
for food in foods:
    print(food, end=": $")
    print(prices[i])
    i += 1
for price in prices:
    total += price
print(f"Total Cost: ${total}")