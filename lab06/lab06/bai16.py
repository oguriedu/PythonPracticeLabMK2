x=int(input("mời nhập X: "))
y=int(input('mời nhập Y: '))
mang_2_chieu = [[0 for cot in range(y)] for hang in range(x)]
for hang in range(x):
    for cot in range(y):
        mang_2_chieu[hang][cot]=hang*cot
print(mang_2_chieu)