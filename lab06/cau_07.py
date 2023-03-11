mon = ["mon", 73]
tue = ["tue", 89]
wed = ["wed", 95]
thu = ["thu", 103]
fri = ["fri", 115]
sat = ["sat", 128]
sun = ["sun", 120]
list_ = [mon, tue, wed, thu, fri, sat, sun]
print("list test:",list_)

y = list_[2][1]
print("Phan tu can tim  la:",y)

x = len(list_)
print("Do dai list test la:",x)
test = ["hungdz", 412]
list_.append(test)
print("List test sau khi them sublist la:",list_)

z = mon[1]
c = tue[1]
v = sun[1]
sum = z+c+v
print("Tong sale value trong ba ngay thu 2, thu 3 va chu nhat la:",sum)
