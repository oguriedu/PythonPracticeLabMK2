#chương trình nhập số và in ra cách đọc tương ứng
n=int(input("nhập số bạn muốn đọc, n= "))
luu_so= list(str(n))

# danh sách các chữ số
doc_so= ["không", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]

# in ra chữ tương ứng với mỗi ký tự trong chuỗi
for luu_so in luu_so:
    print(doc_so[int(luu_so)], end=" ")
