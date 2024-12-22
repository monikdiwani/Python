'''
Q.4) WAP to accept basic salary from user and Give 10% of DA
on basic salary ,12% HRA on basic salary  to employee if the
salary is more than 50000 .calculate total salary.

'''
# Accepting the basic salary from the user
salary = float(input("Enter the basic salary: "))

# Initializing DA and HRA
da = 0
hra = 0

# Check if the basic salary is more than 50000
if salary > 50000:
    # Calculate 10% DA and 12% HRA
    da = 0.10 * salary
    hra = 0.12 * salary

# Calculate the total salary
total_salary = salary + da + hra

# Display the total salary
print("Total Salary:", total_salary)
