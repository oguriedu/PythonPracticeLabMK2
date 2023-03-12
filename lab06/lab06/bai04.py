lst=[]
while True:
    lst=int(input("nhập vào số :"))
    if lst==0:
        print("bạn đã nhập vào giá trị 0")
        break
    lst.append(lst)
lst_mới=[1,2,3]
n=5
for i in lst :
    lst.insert(n,i) 
    n+=1
lst.sort(reserve=True)
for i in lst_mới:
    lst.insert(0,i)
lst_mới.sort()
lst.extend(lst_mới)
print(f"list mới là : {lst} ")   
