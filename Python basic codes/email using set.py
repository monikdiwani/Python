#WAP to accept different email ids of customer(repeat at least 3) in list and
#try to print unique emails

email_list = [
    "monik@gmail.com", "krupa@gmail.com", "shiv@gmail.com","monik@gmail.com", "vrutik@gmail.com", "hariom@gmail.com","shiv@gmail.com", "hariom@gmail.com"]

unique_emails = set(email_list)

print("Unique Email IDs:")
for email in unique_emails:
    print(email)
