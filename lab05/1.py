str = input("hãy nhập 1 chuỗi lí tự str :")
print (" \n \n chuỗi kí tự vừa nhập là :", str)
number = 0
for i in str:
    if i >="0" and i <= "9":
        number+= 1
print (" số các kí tự là số trong chuỗi đã nhập là :", number)