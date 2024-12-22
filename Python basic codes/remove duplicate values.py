#remove deplicate values

def remove_duplicates(l):
    print(list(set(l)))

l=[12,15,89,54,21,21,12]
remove_duplicate(l)

#when to use return
def rem_dup(l2):
    return list(set(l2))

l2=[78,67,89,67,67]

ans=rem_dup(l2)
print("The clean data set is",ans)

