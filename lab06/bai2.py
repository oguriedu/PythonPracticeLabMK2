n=int(input("Nhập số phần tử trog danh sách:"))
lst=[]
for i in range(n):
    x = int(input(f"Nhập phần tử thứ {i+1}: "))
    lst.append(x)
print("Danh sách = ",lst)
# Viết chương trình Python tìm phần tử lớn thứ nhì của danh sách và các vị trí của 
# các phần tử đạt giá trị lớn nhì.
vi_tri=1
lst1=(sorted(lst))[-2]
for i in range(len(lst)):
    if lst[i]==lst1:
        vi_tri+=i
print("Phần tử lớn thứ nhì của danh sách = ",lst1,"ở vị trí thứ",vi_tri)