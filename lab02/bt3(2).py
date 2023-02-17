#Nhập vào chương trình thứ trong tuần và cho biết tên của nó, nếu nhập sai cho phép nhập lại
dic = {1:'Monday',2:'Tuesday',3:'Wednesday',4:'Thursday',5:'Friday',6:'Saturday',7:'Sunday'} 
b = dic.get(a)
while b == None:
    a = int(input('Nhập thứ trong tuần (theo thứ tự 1->7): '))
    print('Thứ',a,'tên là:',b)