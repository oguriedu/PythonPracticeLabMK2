#tính giá trị biểu thức
n=int(input("nhập số nguyên dương n = "))
tongS4=0
while n<=0:
    print("hãy nhập số n thỏa mãn đề bài")
    n=int(input("nhập số nguyên dương n = "))
for i in range(1,n+1):
    tongS4=tongS4+i**2
print("giá trị của biểu thức = ",tongS4)