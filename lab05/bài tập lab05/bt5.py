Str=input('Nhập chuỗi: ')
so=""
chu=""
for c in Str:
    if c.isnumeric():
        so+=c
    else:
        chu+=c
print('Các số trong chuỗi là',so)
tong = 0
for j in range(1, int(so)):
    if (int(so) % j) == 0:
        tong += j
if tong == int(so):
    print('số trên là số hoàn hảo')
else:
    print('số trên không phải số hoàn hảo')
