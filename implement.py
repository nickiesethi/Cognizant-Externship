# Project: Implement Your own Data Structures

print("Welcome to the Inventory Manager!")

inventory = {
    "pineapple" : (2, 2.0),
    "blueberry" : (1, 4.0),
    "strawberry" : (10, 4.0),
    "banana" : (20, 6.0)
}

sum0 = 0
print("\nCurrent Inventory")
for i, (quantity, price) in inventory.items():
    sum0 += price
    print("Item: " + str(i) + ", Quantity: " + str(quantity) + ", Price: $" + str(price))
print("Total value of inventory: " + str(sum0) + "\n")

print("Adding a new item: apple")
inventory["apple"] = (10, 2.0)

print("Updated inventory:")
sum1 = 0
for i, (quantity, price) in inventory.items():
    sum1+=price
    print("Item: " + str(i) + ", Quantity: " + str(quantity) + ", Price: $" + str(price))
print("Total value of inventory: " + str(sum1) + "\n")

print("Deleting an item: banana")
del inventory["banana"]

print("Updated inventory:")

sum = 0
for i, (quantity, price) in inventory.items():
    sum += price
    print("Item: " + str(i) + ", Quantity: " + str(quantity) + ", Price: $" + str(price))
print("Total value of inventory: " + str(sum) + "\n")

print("Updating the price and quantity of pineapple")
inventory["pineapple"] = (21, 9.0)

sum2 = 0
for i, (quantity, price) in inventory.items():
    sum2 += price
    print("Item: " + str(i) + ", Quantity: " + str(quantity) + ", Price: $" + str(price))
print("Total value of inventory: " + str(sum2) + "\n")
