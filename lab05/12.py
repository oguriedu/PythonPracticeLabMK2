# Nhập chuỗi A,B chen '+' để nhận biểu thức C+D=E+F
# Ví dụ: A=’111’ và B=’120’ ➔đẳng thức đúng 1+11=12+0
A = '111'
B = '120'
for i in range(1, len(A)):
    for j in range(1, len(B)):
        C = int(A[:i]) 
        D = int(A[i:])
        E = int(B[:j]) 
        F = int(B[j:])
if C + D == E + F:
    print( str(int(A[:i])) + '+' + str(int(A[i:])) + '=' + str(int(B[:j])) + "+" +str(int( B[j:])))
else:
    print("Không tồn tại cách đặt")