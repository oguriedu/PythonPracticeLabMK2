a=input("Nhập số : ")
if a[0]=='1':
    s=" Một trăm "
elif a[0]=='2':
    s=" Hai trăm "
elif a[0]=='3':
    s=" Ba trăm "
elif a[0]=='4':
    s=" Bốn trăm "
elif a[0]=='5':
    s=" Năm trăm "
elif a[0]=='6':
    s=" Sáu trăm "
elif a[0]=='7':
    s=" Bảy trăm "
elif a[0]=='8':
    s=" Tám trăm "
elif a[0]=='9':
    s=" Chín trăm "
if a[1]=='0':
    if a[2]!='0':
        s+='lẻ '
elif a[1]=='1':
    s+='mười '
elif a[1]=='2':
    s+='hai mươi '
elif a[1]=='3':
    s+='ba mươi '
elif a[1]=='4':
    s+='bốn mươi '
elif a[1]=='5':
    s+='năm mươi ' 
elif a[1]=='6':
    s+='sáu mươi '
elif a[1]=='7':
    s+='bảy mươi '
elif a[1]=='8':
    s+='tám mươi '
elif a[1]=='9':
    s+='chín mươi ' 
if a[2]=='1':
    s+='một '
elif a[2]=='2':
    s+='hai'
elif a[2]=='3':
    s+="ba"
elif a[2]=='4':
    s+='bốn'
elif a[2]=='5':
    s+='năm'
elif a[2]=='6':
    s+='sáu'
elif a[2]=='7':
    s+='bảy'
elif a[2]=='8':
    s+='tám'
elif a[2]=='9':
    s+='chín'
print(s)