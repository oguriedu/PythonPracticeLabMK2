a = [2, -4, 1, 9, -3, 6, 3, -2, 6, 8]
print(a)
# tính tổng các phần tử
print('tổng các phần tử trong list là: ',sum(a))

# số lượng các số hạng dương và tổng các số hạng
j = []
a1 = 0
a2 = 0
for i in a:
    if i > 0:
        j.append(i)
        a1 += 1
print("số lượng các số hạng dương là: ", a1)
print("tổng của các số hạng dương là: ", sum(j))

# tìm vị trí phần tử âm đầu tiên trong danh sách
for i in a:
    a2 += 1
    if i < 0:
        break
print("phần tử âm đầu tiên trong list là: ", a2)

# tìm vị trí phần tử dương cuối cùng trong danh sách
b = a.copy()
b.reverse()
a3 = 0
for i in b:
    if i > 0:
        break
    a3 += 1
print("vị trí phần tử cuối cùng: ", len(a) - a3)
# tìm phần tử lớn nhất trong danh sách và vị trí của nó
b.sort()
a4 = 0
for i in a:
    if i == max(b):
        break
    a4 += 1
print("phần tử lớn nhất trong danh sách là: ", max(b))
print("nằm ở vị trí thứ: ", a4 + 1)