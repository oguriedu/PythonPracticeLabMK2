tenure = int(input("Nhập vào thâm niên công tác (tính bằng tháng): "))
basic_salary = 1350000
if tenure < 12:
    coefficient = 2.34
elif tenure < 36:
    coefficient = 3.33
elif tenure < 60:
    coefficient = 3.66
else:
    coefficient = 3.99
print(f"Lương của nhân viên là: {tenure*basic_salary} đồng")
