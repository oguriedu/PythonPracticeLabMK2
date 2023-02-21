#Nhập số nguyên dương 
n = int(input("Nhập một số nguyên dương: "))

#Khai báo danh sách lưu trữ số nguyên tố 
list_so_nt = []

#Tìm số nguyên tố 
for i in range(2,n+1): flag = 1 
for j in range(2,i): 
    if (i%j==0): flag = 0 
    break

if (flag==1):
    list_so_nt.append(i)
#Phân tích thừa 
dict_phan_tich = {} 
x = n 
for i in list_so_nt: 
    if (x%i==0): count = 0 
    while(x%i==0): count = count + 1 
    x = int(x/i) 
    dict_phan_tich[i] = count

#Xuất kết quả 
print("Dạng phân tích thừa của số ", n, " là: ") 
for k,v in dict_phan_tich.items(): print(k,"^",v,end=" ")