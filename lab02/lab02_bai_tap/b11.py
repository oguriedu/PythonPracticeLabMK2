month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day = int(input("Nhập vào ngày trong tháng: "))
month = int(input("Nhập vào tháng: "))

if day < month_days[month - 1]:
    day = day + 1
else:
    day = 1
    if month == 12:
        month = 1
    else:
        month = month + 1

print(f"Ngày tiếp theo: {day}/{month}")