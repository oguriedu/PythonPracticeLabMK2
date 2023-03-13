str = input("Nhập chuỗi ký tự: ")
new_str = ""
for char in str:
    if char.isdigit():
        new_str = new_str + char

print(f"Chuỗi ký tự mới: {new_str}")
if len(new_str) == 0:
    print("Chuỗi không chứa số")
else:
    num = int(new_str)
    sum = 0
    for i in range(1, num):
        if num % i == 0:
            sum += i
    if num == sum:
        print(f"{num} là số hoàn hảo")