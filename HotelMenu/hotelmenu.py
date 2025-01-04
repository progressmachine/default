menu = {
    'chicken' : 100,
    'egg' : 30
}

print("Welcome to my Restaurant.")
print("Chicken : Rs. 100\nEgg : Rs. 30")

total_cost = 0

while True:
    item = input("Enter your order: ").lower()
    if item in menu:
        total_cost += menu[item]
    else:
        print("Not Available")
    
    while True:
        more = input("Want something else? [y/n]: ").lower()
        if more == 'y':
            another_item = input("Enter your order: ").lower()
            if another_item in menu:
                total_cost += menu[another_item]
            else:
                print("Not Available")
        else:
            break
    
    break

print(f'Total cost is {total_cost}.')