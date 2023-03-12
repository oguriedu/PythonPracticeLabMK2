numbers=[]
while True: 
    n = int(input("Nhập vào một số nguyên (nhập 0 để kết thúc nhập): ")) 
    if n == 0: 
        break 
    numbers.append(n)
num2=[]
num1=[]
for i in numbers:
    if i>0:
        num1.append(i)
    else:
        num2.append(i)
num1.extend(num2)
print(f"Chuyển phần tử dương lên đầu ta có danh sách sau {num1}")
m=int(input('Nhập m: '))
numbers.insert(4,m)
numbers.append(m)
numbers.insert(0,m)
print(f"Chèn m vào đầu, cuối, ví trị thứ 5 ta được danh sách {numbers}")