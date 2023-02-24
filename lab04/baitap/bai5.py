lst=[]
n=int(input("Nhập giá trị : "))
while n>0:
    n=int(input("Tiếp tục nhập giá trị : "))
    lst.append(n)
    if n<0:
        break
print(lst)
