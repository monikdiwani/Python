#WAP to find second largest element

marks=[34,56,23,89,54]

for i in range (0,5):
    for j in range(i+1,5):
        if marks[j]>marks[i]:
            temp=marks[i]
            marks[i]=marks[j]
            marks[j]=temp

print(marks)
print(marks[1])
