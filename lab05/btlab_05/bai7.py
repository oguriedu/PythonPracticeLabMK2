Str="Khoa khoa hoc ung dung"
Str1="khoa"
print("Str:",Str)
print("Str1:",Str1)
count = 0 
start = 0
while True:
    start = Str.find(Str1, start) 
    if start == -1:
        break
    count += 1
    start+=1
if count==0:   
    print("chuỗi Str1 không nằm trong chuỗi Str")
else:
    print("Chuỗi Str chứa",count,"từ đơn",Str1,)