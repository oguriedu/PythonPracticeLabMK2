input_string = input("Nhập vào chuỗi ký tự có độ dài 10 ký tự: ")

sub_string_1 = input_string[2:7]
print("Chuỗi ký tự con từ vị trí thứ 3 đến vị trí thứ 7:", sub_string_1)

sub_string_2 = input_string[:6]
print("Chuỗi ký tự con gồm 06 vị trí kể từ vị trí đầu tiên:", sub_string_2)

sub_string_3 = input_string[-4:]
print("Chuỗi ký tự con từ cuối chuỗi gồm 4 ký tự:", sub_string_3)

reverse_string = input_string[::-1]
print("Đảo ngược chuỗi ký tự nhập vào:", reverse_string)
