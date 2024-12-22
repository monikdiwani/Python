# Function to print the multiplication table of a number
def multiplication_table(num):
    print(f"Multiplication table of {num}:")
    # Loop to generate and print the table
    for i in range(1, 11):
        print(num * i)

# Taking the number as input
num = int(input("Enter a number to get its multiplication table: "))
# Displaying the multiplication table
multiplication_table(num)
