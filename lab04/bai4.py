#nhập vào giá trị của phân số 
a=int(input("nhập tử số của phân số = "))
b=int(input("nhập mẫu số của phân số = "))
while b==0:
    print("nhập không hợp lệ, hãy nhập lại")
    b=int(input("nhập mẫu số của phân số = "))
print("phân số bạn vừa nhập có dạng : ",a,'/',b)