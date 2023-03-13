lst = [int(x) for x in input().split()]
for i in lst:
    assert i%2==0, "Dãy có số lẻ"
print('Dãy chẵn')