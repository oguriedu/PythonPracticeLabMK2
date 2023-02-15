#chương trình tính lương nhân viên
tnct=int(input("mời nhập thâm niên công tác: "))
if tnct<12:
    hs=2.34
elif tnct>=12 and tnct<36:
    hs=3.33
elif tnct>=36 and tnct<60:
    hs=3.66
else:
    hs=3.99
lcb=1350000
luong=hs*lcb
print("lương nhân viên là: ",luong)
