read = ["không", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]
while True:
    n = input("Nhap mot so: ")
    if (n.isnumeric()):
        break

for i in n:
    print(read[int(i)], end=" ")
