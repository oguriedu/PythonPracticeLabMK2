a=[2,-4,1,9,-3,6,3,-2,6,8]
tong=0
duong=0
am=0
for i in a:
    tong+=i
    if i>0:
        duong+=i
for j in a:
    if j<0:
        am+=j
        break
lon_nhat=0
print(tong)
print(duong)
print(am)