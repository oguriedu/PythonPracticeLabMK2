a=(input("nhập số nguyên có ba chữ số: "))
while (int(a)<100)or(int(a)>=1000):
    print("số không thỏa mãn điều kiện")
    a=input("vui lòng nhập lại: ")
tram=["không trăm","một trăm","hai trăm","ba trăm","bốn trăm","năm trăm","sáu trăm","bảy trăm","tám trăm","chín trăm"]
chuc=["lẻ","mười","hai muơi","ba muơi","bốn muơi","năm muơi","sáu muơi","bảy muơi","tám muơi","chín muơi"]
dv=["không","một","hai","ba","tư","năm","sáu","bảy","tám","chín"]

if a[2]== "0" and a[1]=="0":
    print(tram[int(a[0])])
elif a[2]=="0":
    print(tram[int(a[0])],chuc[int(a[1])])
else :
    print(tram[int(a[0])],chuc[int(a[1])],dv[int(a[2])])
