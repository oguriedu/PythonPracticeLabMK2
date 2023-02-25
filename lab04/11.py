while True:

 print("Menu của chúng ta có các loại thức uống sau:") 
 print("1. Cam vắt") 
 print("2. Nước ép cà rốt") 
 print("3. Nước lọc") 
 print("4. Nước dừa") 
 
try: user_choice = int(input("Xin mời bạn chọn một thức uống: ")) 
if user_choice == 1: print("Bạn đã chọn cà phê cam vắt!") 
elif user_choice == 2: print("Bạn đã chọn nước ép cà rốt!") 
elif user_choice == 3: print("Bạn đã chọn nước lọc!") 
elif user_choice == 4: print("Bạn đã chọn nước dừa!")
else: print("Hãy chọn một số từ 1 đến 4 để chọn thức uống của bạn.") 
except ValueError: 
print("Hãy nhập vào số từ 1 đến 4.")