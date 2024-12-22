# Create a dictionary of customer IDs and their names
customers = {
    101: "Monik",
    102: "Tony",
    103: "Charlie",
    104: "Steve",
    105: "Paper"
}

# 1. Display all customer IDs and their names
print("Customer IDs and their names:")
for customer_id, name in customers.items():
    print(customer_id, name)

# 2. Add a new customer
customers[106] = "Thor"
print("\nAdded a new customer:")
print(customers)

# 3. Update the name of an existing customer
customers.update({103: "Happy"})
print("\nUpdated customer name for ID 103:")
print(customers)

# 4. Remove a customer
customers.pop(102)
print("\nRemoved customer with ID 102:")
print(customers)

# 5. Display all customer IDs and their names again after updates
print("\nUpdated customer list:")
for customer_id, name in customers.items():
    print(customer_id, name)
