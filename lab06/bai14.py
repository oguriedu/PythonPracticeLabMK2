import re

def is_valid_password(password):
    # Kiểm tra độ dài mật khẩu
    if len(password) < 6 or len(password) > 12:
        return False
    # Kiểm tra các tiêu chí đặc biệt
    if not re.search("[a-z]", password):
        return False
    if not re.search("[0-9]", password):
        return False
    if not re.search("[A-Z]", password):
        return False
    if not re.search("[$#@]", password):
        return False
    # Nếu các tiêu chí được đáp ứng, mật khẩu đó là hợp lệ
    return True

# Nhập danh sách mật khẩu từ người dùng, được phân tách bằng dấu phẩy
passwords = input("Nhập danh sách mật khẩu, phân tách bằng dấu phẩy: ").split(",") 

# Lặp qua mỗi mật khẩu và kiểm tra tính hợp lệ
valid_passwords = []
for password in passwords:
    password = password.strip()
    if is_valid_password(password):
        valid_passwords.append(password)

# In ra danh sách mật khẩu hợp lệ
print("Mật khẩu hợp lệ: ", end="")
print(*valid_passwords, sep=", ")