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
print(numbers)