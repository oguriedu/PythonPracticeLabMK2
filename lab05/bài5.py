#in ra chuỗi số và kiểm tra hoàn hảo của chuỗi số đó
s = input("Nhập chuỗi ký tự = ")
#xóa kí tự
s = "".join(filter(str.isdigit, s))
print("chuỗi kí tự vừa nhập là",s)
so=int(s)
tong=0
for i in range(1,so):
    if so % i ==0:
        tong+=i
if tong==so:
    print(so,"là số hoàn hảo")
else:
    print(so,"không là số hoàn hảo")
