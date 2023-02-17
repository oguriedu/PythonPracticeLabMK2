'''
viết chương trình tính tổng nghịch đảo
'''
n = int(input("nhập n: "))
a = 0
for i in range(1,n):
    a = a + 1/i
print(a)