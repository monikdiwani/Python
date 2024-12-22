# Create a dictionary of products with their prices
supermarket = {
    "Milk": 50,
    "Eggs": 120,
    "Bread": 40,
    "Butter": 200,
    "Sugar": 45
}

# 1. Display all products with their prices
print("Products in the supermarket:")
for product, price in supermarket.items():
    print(product, price)
    
# 2. Add a new product
supermarket["Cheese"] = 150
print("\nAdd a new product:")
print(supermarket)

# 3. Update the price of an existing product
supermarket.update({"Sugar": 50})

# 4. Remove a product
supermarket.pop("Eggs")  

# 5. Display all products again after updates
print("\nUpdated products in the supermarket:")
for product, price in supermarket.items():
    print(product, price)
