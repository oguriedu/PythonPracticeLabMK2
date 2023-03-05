ky_tu="100010101"
tong=0
for i in range(len(ky_tu)):
    tong += int(ky_tu[i]) * (2**(len(ky_tu) - i -1))
print("Số nhị phân",ky_tu,"chuyển sang số thập phân =",tong)