ky_tu="11100"
sum=0
for i in range(len(ky_tu)):
    sum += int(ky_tu[i]) * (2**(len(ky_tu) - i -1))
print("Số nhị phân",ky_tu,"chuyển sang số thập phân =",sum)
