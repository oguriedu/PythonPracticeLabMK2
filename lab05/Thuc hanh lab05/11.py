a=input("nhập dãy ký tự liên tiếp: ")
x=''
for i in a:
    if i==" " or i ==",":
        if x !="":
            print(x)
        x=''
    else:
        x+=i
else:
    if x !="":
            print(x)