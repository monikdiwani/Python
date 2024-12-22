# Function to check voting eligibility
def can_vote(age):
    if age >= 18:
        return "You can vote."
    else:
        return "You cannot vote."

# Taking the age as input
age = int(input("Enter your age: "))
# Checking and displaying whether the person can vote
print(can_vote(age))
