'''WAP to generate electricity bill '''

unit = int(input("Enter your electricity consumption in units: "))

if unit > 0 and unit <= 100:
    bill = unit * 10
    print("Your bill is", bill)
elif unit > 100 and unit <= 200:
    bill = 100 * 10 + (unit - 100) * 15
    print("Your bill is", bill)
elif unit > 200 and unit <= 300:
    bill = 100 * 10 + 100 * 15 + (unit - 200) * 20
    print("Your bill is", bill)
else:
    bill = 100 * 10 + 100 * 15 + 100 * 20 + (unit - 300) * 25
    print("Your bill is", bill)
