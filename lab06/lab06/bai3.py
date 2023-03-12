n=int(input("mời nhập số tự nhiên n: "))
danh_sach=[]
#nhập danh sách
while n!=0:
    danh_sach.append(n)
    n=int(input("mời nhập số tự nhiên n: "))
    if n==0:
        danh_sach.append(n)
        break
#chuyển phần tử dương lên đầu và in 
b=danh_sach.copy()
b.sort()
b.reverse()
print(b)
#m nhập từ bàn phím:
m=int(input('mời nhập m: '))
danh_sach.insert(4,m)
danh_sach.insert(0,m)
danh_sach.append(m)
print(danh_sach)

