str =input(" nhập chuỗi kí tự str :")
print (" chuỗi ký tự vừa nhập là :", str)
count= 0
nonumbers= 0
for i in str:
    if not (i >= "a" and  i <= "z") or ( i >= "A" and i <= "Z"):
        count +=1
print (" sóo kt k phải là chữ cái t.anh là :", count)
for j in str:
    if not ( j>= "0" and j <= "9"):
        nonumbers +=1
print (" sóo kt k phải số là :", nonumbers)
