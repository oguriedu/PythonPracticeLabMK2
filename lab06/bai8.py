n=int(input('Nhập n: '))
s = [0, 1]
s += [(s == [s[1], s[0] + s[1]]) and s[1] for j in range(n-1)]
for i in s:
    if i==s[-1]:
        print(i)
        break
    else:
        print(i,end=',')