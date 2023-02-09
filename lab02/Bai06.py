a=input("Nhập số có 3 chữ số : ")
if a[0]=='1':
    b=" Một trăm "
elif a[0]=='2':
    b=" Hai trăm "
elif a[0]=='3':
    b=" Ba trăm "
elif a[0]=='4':
    b=" Bốn trăm "
elif a[0]=='5':
    b=" Năm trăm "
elif a[0]=='6':
    b=" Sáu trăm "
elif a[0]=='7':
    b=" Bảy trăm "
elif a[0]=='8':
    b=" Tám trăm "
elif a[0]=='9':
    b=" Chín trăm "
if a[1]=='0':
    if a[2]!='0':
        b+='lẻ '
elif a[1]=='1':
    b+='mười '
elif a[1]=='2':
    b+='hai mươi '
elif a[1]=='3':
    b+='ba mươi '
elif a[1]=='4':
    b+='bốn mươi '
elif a[1]=='5':
    b+='năm mươi ' 
elif a[1]=='6':
    b+='sáu mươi '
elif a[1]=='7':
    b+='bảy mươi '
elif a[1]=='8':
    b+='tám mươi '
elif a[1]=='9':
    b+='chín mươi ' 
if a[2]=='1':
    b+='một '
elif a[2]=='2':
    b+='hai'
elif a[2]=='3':
    b+="ba"
elif a[2]=='4':
    b+='bốn'
elif a[2]=='5':
    b+='năm'
elif a[2]=='6':
    b+='sáu'
elif a[2]=='7':
    b+='bảy'
elif a[2]=='8':
    b+='tám'
elif a[2]=='9':
    b+='chín'
print(b)