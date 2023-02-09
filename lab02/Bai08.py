tnct=float(input("Nhập thâm niên công tác: "))
lcb=1350000
if tnct<12:
    l=lcb*2.34
elif tnct<36:
    l=lcb*3.33
elif tnct<60:
    l=lcb*3.66
else:
    l=lcb*3.99
print("Lương: ",l,'vnđ')