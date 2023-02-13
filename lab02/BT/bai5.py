a=int(input("nhập tháng: "))
while (a>=13)and(a<0):    
    a=int(input("nhập lại tháng: "))
t=['january','february',"march",'april',"may","june",'july','august',"september","october","november","december"]
a=a-1
print(t[a])