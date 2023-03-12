import re 
tk=input("Nhap ten tai khoan:")
mk=input("Nhap mat khau:")
kmk=mk.split(",")
mkk=[]
for km in kmk:
    if len(km)<6 or len(km)>12:
        continue 
    elif not re.search("[a-z]",km):
        continue
    elif not re.search("[A-Z]",km):
        continue
    elif not re.search("[0-9]",km):
        continue
    elif not re.search("[@#$]",km):
        continue
    else :
        mkk.append(km)
print(mkk)
