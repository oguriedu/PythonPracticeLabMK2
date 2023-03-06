lst = []
string = input("nhập kí tự: ")
for a in string:
    a = string.isalnum()
    if a == True: 
        lst.append(a)
print(len(str(lst)))