n = input("Nhap day ky tu lien tiep: ")
x = ''
for i in n:
    if i == " " or i == ",":
        if x != "":
            print(x)
        x = ''
    else:
        x += i
else:
    if x != "":
            print(x)