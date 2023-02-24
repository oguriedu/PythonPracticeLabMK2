a = int(input("Nhập vào số nguyên thứ nhất: ")) 
b = int(input("Nhập vào số nguyên thứ hai: "))

if a > b: small = b 
else: small = a

while(True): 
    if((small % a == 0) and (small % b == 0)): bội_chung_nhỏ_nhất = small 
    break 
small = small + 1

print("Bội chung nhỏ nhất của hai số nguyên là", bội_chung_nhỏ_nhất)