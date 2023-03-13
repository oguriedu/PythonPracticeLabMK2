# c1
input_string = input("Nhập chuỗi ký tự: ")

# Loại bỏ các khoảng trắn ở đầu và cuối chuỗi ký tự
while len(input_string) > 0 and input_string[0] == " ":
    input_string = input_string[1:]
while len(input_string) > 0 and input_string[-1] == " ":
    input_string = input_string[:-1]

# Chuyển tất cả các ký tự trong chuỗi sang chữ thường
input_string = input_string.lower()

# Thay thế nhiều khoảng trắng thừa ở giữa các từ bằng một khoảng trắng
normalized_string = ""
for i in range(len(input_string)):
    if input_string[i] != " " or (input_string[i] == " " and
                                  input_string[i-1] != " "):
        normalized_string += input_string[i]
# Print the normalized string
print("Chuỗi ký tự sau khi được chuẩn hóa là:", normalized_string)

# c2
input_string = input("Nhập vào một chuỗi ký tự: ")

# Dùng hàm strip() để loại bỏ khoảng trắng ở đầu và cuỗi chuỗi
input_string = input_string.strip()

# Chuyển tất cả các ký tự sang chữ thường
input_string = input_string.lower()

# "Thay thế các khoảng trắng bằng một khoảng trắng duy nhất"
input_string = " ".join(input_string.split())

# In ra màn hình chuỗi sau khi đa chuẩn hóa
print("Normalized string:", input_string)
