'''Viêts chương trình nhập sô KƯ điện tiêu thụ
tính tiền điện'''
while True:
    print("Nếu số KW: 0 -> 100: đơn giá 2000 đồng/KW.")
    print("Nếu số KW: 101 -> 200: đơn giá 2500 đồng/KW.")
    print("Nếu số KW: 201 -> 300: đơn giá 3000 đồng/KW.")
    print("Nếu số KW: > 300: đơn giá 5000 đồng/KW.")
    print("----------------------------------------------")
    choice=int(input("Nhập số KW điện tiêu thụ:"))
    if 0<choice<100:
        print("Với",choice,"KW điện tiêu thụ, tiền điện =",choice*2000)
    if 101<choice<200:
        print("Với",choice,"KW điện tiêu thụ, tiền điện =",choice*2500)
    if 201<choice<300:
        print("Với",choice,"KW điện tiêu thụ, tiền điện =",choice*3000)
    if choice>300:
        print("Với",choice,"KW điện tiêu thụ, tiền điện =",choice*5000)
    print("---------------------------------------------")