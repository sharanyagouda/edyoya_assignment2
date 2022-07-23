
lst=int(input("enter size of list"))
data=int(input("enter size of list"))
lst1=[]
for i in range(lst):
    res=int(input("enter elements"))
    lst1.append(res)
print(lst1)  
lst2=[]
for j in range(data):
    res1=int(input("enter elements"))
    lst2.append(res1)
print(lst2) 
lst3=list(zip(lst1,lst2))  
print(lst3) 
lst3.sort(key=lambda x:x[1])
print(lst3)
