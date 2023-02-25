# Nhập một số thập phân và sau đó chuyển đổi số đó thành dạng ký tự
n=float(input("Nhập 1 số bất kỳ:"))
print(n)
lst=[]
ky_tu={1:"Một",2:"Hai",3:"Ba",4:"Bốn",5:"Năm",6:"Sáu",7:"Bảy",8:"Tám",9:"Chín",0:"Không",}
for i in str(n):
    if i ==".":
        continue
    else:
        lst.append(i)
for i in lst:
    for j in ky_tu.keys():
        if float(i)==j:
            print(ky_tu[j],end=" ")
        

    
    
    

