numbers=[]
while True: 
    number = int(input("Nhập vào một số nguyên (nhập 0 để kết thúc nhập):")) 
    if number == 0: 
        break 
    numbers.append(number)
numbers2=[]
numbers1=[]
for i in numbers:
    if i>0:
        numbers1.append(i)
    else:
        numbers2.append(i)
numbers1.extend(numbers2)
print(f"Chuyển phần tử dương lên đầu ta có danh sách sau {numbers1}")
m=int(input('Nhập m: '))
numbers.insert(4,m)
numbers.append(m)
numbers.insert(0,m)
print(f"Chèn m vào đầu, cuối, ví trị thứ 5 ta được danh sách {numbers}")