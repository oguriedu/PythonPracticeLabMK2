A = input('nhập chuỗi A:')
B = input('nhập chuỗi B:')
flag = False
try:
    for i in range(1,len(A)):
        sumA = int(A[:i]) + int(A[i:])
        for j in range(1,len(B)):
            sumB = int(B[:j]) + int(B[j:])
            if sumA == sumB:
                print(f'đẳng thức đúng {int(A[:i])} + {int(A[i:])} = {int(B[:j])} + {int(B[j:])}')
                flag = True
                break
except:
    pass
            
if flag == False:
    print('không tồn tại cách đặt!')