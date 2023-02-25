# Chương trình nhập tử số mẫu số của 1 phân số
mau_so=int(1)
while  mau_so >0:
    tu_so=int(input("Nhập tử số:"))
    mau_so=int(input("Nhập mẫu số:"))
    if mau_so==0:
        mau_so=int(input("Nhập lại mẫu số khác 0:"))
    print(tu_so,"/",mau_so)
      


