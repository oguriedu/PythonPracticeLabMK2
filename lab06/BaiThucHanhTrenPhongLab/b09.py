a = [2,4,6,8]
print(a)
b = [1,2,3,4,5,6,7,8,9]
print(b)

for num in a:
    assert num%2 == 0, "day co chua so le"
else:
    print("Day chi chua so chan")


for num in b:
    assert num%2 == 0, "day co chua so le"
else:
    print("Day chi chua so chan")
