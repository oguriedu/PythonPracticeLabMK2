n = int(input('Nhập số lượng tuple: '))
danh_sach = []
for i in range(n):
    name = input('Nhập tên: ')
    age = int(input('Nhập tuổi: '))
    score = float(input('Nhập điểm: '))
    danh_sach.append((name, age, score))

def sort_key(item):
    name = item[0]
    age = item[1]
    score = item[2]
    return (name, age, score)
sorted_danh_sach = sorted(danh_sach, key=sort_key)

print('Danh sách đã sắp xếp:')
for item in sorted_danh_sach:
    print(item)
