import re
password = input("hãy nhập mật khẩu: ")
#a
if re.search(r'[a-z]', password):
    print("Mật khẩu hợp lệ!")
else:
    print("Mật khẩu không hợp lệ!")
#b
if re.search(r'[0-9]', password):
      print("Mật khẩu hợp lệ!")
else:
    print("Mật khẩu không hợp lệ!")
#c
if re.search(r'[A-Z]', password):
      print("Mật khẩu hợp lệ!")
else:
    print("Mật khẩu không hợp lệ!")
#d
if re.search(r'[$ @ #]', password):
      print("Mật khẩu hợp lệ!")
else:
    print("Mật khẩu không hợp lệ!")