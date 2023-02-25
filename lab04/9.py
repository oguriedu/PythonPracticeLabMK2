# Tính tổng các chữ số vừa nhập
n=int(input("Nhập 1 số bất kỳ:"))
tong=[]
for i in str(n):
    tong.append(int(i))

print("Tổng các chữ số của số",n,"=",sum(tong))