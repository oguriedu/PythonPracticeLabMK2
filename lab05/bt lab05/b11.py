a=input("nhập dãy ký tự liên tiếp : ")
b=''
for i in a:
    if i==" " or i ==",":
        if b !="":
            print(b)
        b=''
    else:
        b+=i
else:
    if b !="":
            print(b)