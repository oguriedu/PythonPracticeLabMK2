R=float(input("nhap ban  kinh cua khoi tru :"))
H=float(input("nhap duong cao cua khoi tru :"))
𝝅=3.14
dien_tich_xung_quanh=2*𝝅*float(R*H)
dien_tich_toan_phan=2*𝝅*R**2+dien_tich_xung_quanh
the_tich=H*3.14*R**2
print("dien tich xung quanh cua hinh tru la :",dien_tich_xung_quanh)
print("dien tich toan phan cua hinh tru la :",dien_tich_toan_phan)
print("the tich cua hinh tru la :",the_tich)