lst=[]
while True:
   x=int(input("Nhập giá trị : "))
   if x==0:
      break
   lst.append(x)
print("lst vừa nhập : ",lst)
lst1=[]
lst2=[]
for i in lst:
   if i>0:
        lst1.append(i)
   else:
       lst2.append(i) 
lst1.extend(lst2)
print("Danh sách sau khi chuyển phần tử dương lên đầu là : ",lst1)

m = input("Nhập số cần chèn: ")
lst.insert(0,m)
print("Danh sách sau khi chèn", m, "vào đầu danh sách là:")
print(lst)
lst.append(m)
print("Danh sách sau khi chèn", m, "vào cuối danh sách là:")
print(lst)
if len(lst) >= 5:
    lst.insert(4, m)
    print("Danh sách sau khi chèn", m, "vào vị trí thứ 5 là:")
    print(lst)
else:
    print("Danh sách không đủ dài để chèn vào vị trí thứ 5.")