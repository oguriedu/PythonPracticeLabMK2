a=input('nhap chuoi a :')
b=input('nhap chuoi b :')

m = len(a)
n = len(b)
counter = [[0]*(n+1) for x in range(m+1)]
longest = 0
lcs_set = set()
for i in range(m):
    for j in range(n):
        if a[i] == b[j]:
            c = counter[i][j] + 1
            counter[i+1][j+1] = c
            if c > longest:
                lcs_set = set()
                longest = c
                lcs_set.add(a[i-c+1:i+1])
            elif c == longest:
                lcs_set.add(a[i-c+1:i+1])
for s in lcs_set:
    print(s)