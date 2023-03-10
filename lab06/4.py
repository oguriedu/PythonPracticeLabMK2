numbers=[]
while True: 
    number = int(input("Nhập vào một số nguyên (nhập 0 để kết thúc nhập): ")) 
    if number == 0: 
        break 
    numbers.append(number)
lst=[1,2,3]
n=5
for i in lst:
    numbers.insert(n,i)
    n+=1
lst.sort(reverse=True)
for i in lst:
    numbers.insert(0,i)
lst.sort()
numbers.extend(lst)
print('Sau khi chèn danh sách [1,2,3] vào vị trí đầu, cuối, thứ 5 ta được danh sách',numbers)
k=int(input('Nhập vị trí cần xóa:  '))
lst2=numbers.pop(k)
print(f"Phần tử thứ {k} là {lst2} đã bị xóa khỏi list")
print('List sau khi sắp xếp theo thứ tự tăng dần là',sorted(numbers))
print('List sau khi sắp xếp theo thứ tự giảm dần là',sorted(numbers,reverse=True))

