def kiem_tra_so(n):
    dic = {1:"một", 2:"hai", 3:"ba", 4:"bốn", 5:"năm", 6:"sáu", 
    7:"bảy", 8:"tám", 9:"chín"}
    a = []
    for i in n:
        a.append(dic[int(i)])
    return" ".join(a)
n = str(input("Nhập giá trị: "))
print(kiem_tra_so(n))

            
