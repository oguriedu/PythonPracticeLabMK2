#Kiểm tra năm nhuận
print('Chương trình kiểm tra một năm có phải là năm nhuận không: ') 
print('Nhập năm cần kiểm tra:', end='')
n=int(input())
if (n%4==0 and n%100 !=0 ) or n%400==0:
  print("Năm ",n,"là năm nhuân!") 
else:
  print('Năm ',n,'không phải là năm nhuận!')