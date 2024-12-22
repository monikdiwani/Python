#Q.1)WAP to calculate simple interest.

# Prompt the user to enter the principal amount and time in years
principle = int(input("Enter the principal amount: "))
time = int(input("Enter the time (in years): "))

# Define the rate of interest (in percent)
rate = 2.5

# Calculate simple interest using the formula: (principal * time * rate) / 100
simple_interest = (principle * time * rate) / 100

# Display the calculated simple interest
print("The simple interest is", simple_interest)