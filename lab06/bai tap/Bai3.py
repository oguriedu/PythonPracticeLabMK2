lst = []
while True:
    num = int(input("Nhập một số tự nhiên (nhập 0 để kết thúc): "))
    if num == 0:
        break 
    lst.append(num) 
print("Danh sách các số đã nhập:", lst)
#Viết chương trình Python chuyển các phần tử dương của danh sách lên đầu danh sách và in danh sách ra màn hình.
def phan_tu_duong(lst):
    return abs(num>0)
lst.sort(key = phan_tu_duong)
lst.sort(reverse = True)
print("Danh sách mới",lst)
#Chèn một số m (m nhập vào từ bàn phím ) vào đầu danh sách, cuối danh sách và vị trí thứ 5 của danh sách.
m=int(input("Nhập số :"))
lst.insert(0, m)
lst.append(m)
lst.insert(4, m)
print("Danh sách mới là:", lst)