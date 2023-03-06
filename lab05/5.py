""" Xóa đi tất cả các ký tự Str không phải là số, 
chuỗi ký tự còn lại sẽ là số và cho biết chuỗi số 
đó là số hoàn hảo hay không
"""
Str=input("Nhập chuỗi ký tự:")
print("Chuỗi ký tự vừa nhập là:",Str)
tong=0
for i in Str:
    if "a" <=i<="z" or "A"<=i<="Z":
        del i
    else:
        if "1" <=i<="9":
            num=0
            tong*=0
            
            for j in range(len(i)):
                num+=int(i[j])
                for k in range(1,num):
                    if num % k==0:
                        tong=tong+k
                if tong == num:
                    print(num,"là số hoàn hảo")
                else:
                    print(num,"không phải là số hoàn hảo")
             
   

                    
        

