n = int(input('nhập số n nguyên dương = '))
tong = 0 
while n<=0:
    print("hãy nhập số thỏa mãn yêu cầu đề bài")
    n=int(input("nhâp số n nguyên dương = "))
for i in range(1, n+1):
    if i % 2 == 0:
        tong -= 1/i
    else:
        tong += 1/i
print(tong)
