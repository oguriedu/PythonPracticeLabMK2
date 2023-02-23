#tính giá trị biểu thức
n=int(input("nhập số nguyên dương n = "))
tongS5=0
while n<0:
    print("hãy nhập số n thỏa mãn đề bài")
    n=int(input("nhập số nguyên dương n = "))
for i in range(0,n+1):
    tongS5=tongS5+(2*i+1)**3
print("giá trị của biểu thức = ",tongS5)