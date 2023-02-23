n = int(input("Nhập giá trị n =  "))
tongS2= 0
for i in range(2, n+1):
    tongS2 += 1/((i-1)*i)
print("Giá trị của S là:", tongS2)
