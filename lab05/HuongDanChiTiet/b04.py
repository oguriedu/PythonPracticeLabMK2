Str = input('Nhập biểu thức ')
n = len(Str)
kt = int(0)
for i in range(0, n):
    if Str[i] == '(':
        kt += 1
    if Str[i] == ')':
        kt -= 1
    if kt < 0:
        break
if kt != 0:
    print('Biểu thức không đúng! ')
else:
    print('Biểu thức đúng!')
