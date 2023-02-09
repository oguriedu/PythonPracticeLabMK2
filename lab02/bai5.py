#chương trình cho biết tháng trong một năm:
thang_trong_nam={1:"January",2:"February",3:"March",4:"April",5:"May",6:"June",7:"July",8:"August",9:"Septe",10:"October",11:"November",12:"December"}

while True:
    thang=int(input(" Hãy nhập tháng : "))
    if thang in thang_trong_nam:
        break
    print("bạn đã nhập sai,vui lòng nhập lại cho đúng ")
print("tháng bạn vừa nhập là : ",thang_trong_nam[thang])