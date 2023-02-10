thang=int(input('mời nhập tháng: '))
thang_trong_nam=["January","February","March","April","May","June","July","August","September","October","November","December"]
if thang<1 or thang>12:
    while thang not in range(1,13):
        thang=int(input('mời bạn nhập lại: '))
for i in range(1,len(thang_trong_nam)+1):
    if thang==i:
        print(thang_trong_nam[thang-1])


