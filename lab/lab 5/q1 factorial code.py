# Function to calculate the factorial of a number
def factorial(num):
    # Initialize the result as 1 (since factorial of 0 is 1)
    result = 1
    # Loop to calculate factorial
    for i in range(1, num + 1):
        result *= i
    return result

# Taking input from the user
num = int(input("Enter a number to find its factorial: "))
# Displaying the result
print(f"The factorial of {num} is {factorial(num)}")
