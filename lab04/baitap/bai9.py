# bài 9
sum=0
while True:
    i=int(input("nhập số bất kỳ: "))
    sum+=i
    i=input("tiếp tục nhập nhấn 0 : ")
    if i=='0':
        break
print('tổng các chữ số vừa nhập là:',sum)