import random
lst=[]
for i in range(1000):
    r=random.randint(0,99999)
    lst.append(r)
#Cách 1
# print(sorted(lst))
#Cách 2
for i in range(len(lst)): 
    for j in range(i+1, len(lst)): 
        if lst[i] > lst[j]: 
            lst[i], lst[j] = lst[j], lst[i]  
print("Danh sách sau khi sắp xếp:", lst)