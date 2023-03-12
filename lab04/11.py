str=input('nhập một chuỗi số: ')

#xóa các ký tự không phải số
number_str = ""
for chat in str:
    if chat.isdigit():
        number_str += chat

print('chuỗi số vừa nhập là: ',number_str)
#kiểm tra số ký tự số trong chuỗi
number = int(number_str)
dem=0
for i in range(1,number+1):
    if number%i==0:
        dem+=1
if dem==number:
    print('chuỗi số vừa nhập là số hoàn hảo')
else:
    print('chuỗi số vừa nhập không phải là số hoàn hảo')       