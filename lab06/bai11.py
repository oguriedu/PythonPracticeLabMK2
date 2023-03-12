
ls_a = []
while True:
    a = int(input('nhập phần tử trong list(nhập 0 để dừng lại):'))
    if a == 0:
        break
    else:
        ls_a.append(a)
        
print('list vừa nhập',ls_a)
ls_b = [i for i in ls_a if i % 5 != 0 and i % 3 == 0] 
print('list B:',ls_b)
ls_c = [i**2 for i in ls_a]
print('list C:',ls_c)
ls_d = [i for i in ls_a if i % 3 == 0]
print('list D:',ls_d)

