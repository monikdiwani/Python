sports1={"Sanoj","Neha","Dev","Raj","Shweta","Hiral"}
sports2={"Neha","Shweta","Hiral","Arjun","Ram","Sahyog"}

#find total participants in the sports list

Total_Ath=sports1|sports2
print("Total participants:",Total_Ath)

for s in Total_Ath:
    print(s)

#Set difference
New_sports1=sports1-sports2
print("The new sports one list is:",New_sports1)

#WAP to accept different email ids of customer(repeat at least 3) in list and
#try to print unique emails
