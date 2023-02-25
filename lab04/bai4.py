while True:
    numerator = int(input("Nhập tử số: "))
    denominator = int(input("Nhập mẫu số: "))
    if denominator == 0:
        print("Mẫu số không thể bằng 0, vui lòng nhập lại.")
    else:
        break
fraction = numerator / denominator
print("Phân số {}/{} = {}".format(numerator, denominator, fraction))
