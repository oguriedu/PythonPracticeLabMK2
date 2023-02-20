#tính giá trị biểu thức
n=int(input("nhập số n nguyên dương ="))
tongS4=0
while n<=0:
    print("hãy nhập số n thỏa mãn đề bài")
    n=int(input("nhập số n nguyên dương "))
for i in range(1,n+1):
    i=i**2
    tongS4=tongS4+i
print("giá trị của biểu thức s4 = ",tongS4)
