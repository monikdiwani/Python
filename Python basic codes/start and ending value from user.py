#WAP to generate even numbers between 1 and 20
#the ending value is not taken by the system so you have to +1 in loop

start=int(input("Enter starting value :"))
end=int(input("Enter ending value :"))
for i in range (start,end+1):
    if i%2==0:
        print(i)
