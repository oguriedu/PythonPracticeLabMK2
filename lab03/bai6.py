#chương trình tính tổng bậc 3 của n số nguyên đầu tiên
n=int(input("nhập n: "))
m=0
for i in range(n):
    i+=1
    m+=i**3
print("tổng bậc 3 của ",n," số nguyên đầu tiên là",m)