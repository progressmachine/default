price1 = 3.14159
price2 = -987.678
price3 = 123.456

print(f"Price 1 is ${price1:.2f}.")
print(f"Price 2 is ${price2:.1f}.")
print(f"Price 3 is ${price3:.5f}.")

print(f"Price 1 is ${price1:10}.")
print(f"Price 2 is ${price2:3}.") # has 8 but wrote 3, but still prints all
print(f"Price 3 is ${price3:010}.")

print(f"Price 1 is ${price1:<10}.")
print(f"Price 1 is ${price1:<010}.")
print(f"Price 2 is ${price2:>10}.") # has 8 but wrote 3, but still prints all
print(f"Price 3 is ${price3:>010}.")

print(f"Price 1 is ${price1:^10}.")
print(f"Price 1 is ${price1:^010}.")
print(f"Price 1 is ${price1:+}.")

print(f"Price 1 is ${price1: }.")
print(f"Price 2 is ${price2:+}.") # does not do anything 'cause price2 is negative.
print(f"Price 3 is ${price3: }.")

price1 = 300000.14159
price2 = -9870000.678
price3 = 12334523452345.4564234523452345

print(f"Price 1 is ${price1:,}.")
print(f"Price 2 is ${price2:,}.")
print(f"Price 3 is ${price3:+040,.2f}.")