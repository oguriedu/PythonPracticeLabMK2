n = int(input("Nhập số phần tử trong danh sách: "))
lst = []
for i in range(n):
    num = int(input("Nhập một số tự nhiên: "))
    lst.append(num)
#Tìm phần tử thứ hai và vị trí của nó
largest = max(lst)
second_largest = -float('inf')
idx = []
for i, num in enumerate(lst):
    if num > second_largest and num < largest:
        second_largest = num
        idx = [i]
    elif num == second_largest:
        idx.append(i)
      
print("phần tử thứ hai là", second_largest)
print("nó được tìm thấy ở vị trí :", idx)
#Tính số lượng các số dương liên tiếp có tổng lớn nhất
max_sum = 0
consec = 0
for num in lst:
    if num > 0:
        consec += num
        max_sum = max(max_sum, consec)
    else:
        consec = 0
print("số lượng các số dương liên tiếp có tổng lớn nhất là", max_sum)
#tính các số lượng dương liên tiếp có độ dài lớn nhất
max_len = 0
consec = 0
for num in lst:
    if num > 0:
        consec += 1
        max_len = max(max_len, consec)
    else:
        consec = 0

print("số lượng dương liên tiếp có đọ dài lớn nhất", max_len)