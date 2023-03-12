a=[2, -4, 1, 9, -3, 6, 3, -2, 6, 8]
print("Danh sách:",a)
# Viết chương trình Python tính tổng các phần tử của danh sách
print("Tổng các phần tử của danh sách",sum(a))
# Viết chương trình Python đếm số lượng các số hạng dương và tổng của các số hạng dương.
tong=0
dem=0
print("các số hạng dương:")
for i in range (len(a)):
    num=a[i]
    if num>0:
        print(num,end=",")
        dem+=1
        tong+=num
print("\nSố lượng các số hạng dương:",dem)
print("Tổng các số hạng dương =",tong)
# Tìm vị trí của phần tử âm đầu tiên trong danh sách.
for i in range(len(a)):
    if a[i]<0:
        print("vị trí của phần tử âm đầu tiên trong danh sách:", i+1)
        break
# Tìm vị trí của phần tử dương cuối cùng trong danh sách.
for i in range(len(a)):
    if a[i]>0:
        i+=1
print("vị trí của phần tử dương cuối cùng trong danh sách:",i)
# Tìm phần tử lớn nhất của danh sách và vị trí phần tử lớn nhất cuối cùng. 
max_a = max(a)
last = 1
for i in range(len(a)):
    if a[i] == max_a:
        last+= i
print("Phần tử lớn nhất là", max_a,"vị trí thứ",last,"trong danh sách")