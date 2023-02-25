n=int(input('nhập n: '))
if n<=0:
    print('vui lòng nhaajp lại')
    n=int(input('nhập lại n:'))
A=0
B=0
C=0
for i in range(1,n+1):
    A+=i
print("Tổng S1=",A)

for j in range(1,2*n+2,2):
    B+=j
print('Tổng S2 =',B)

for k in range(2,2*n+1,2):
    C+=k
print(f'Tổng S3 = {C}')

