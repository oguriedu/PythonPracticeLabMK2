def number_to_text(number):
    num_to_text = {
        '0': 'không',
        '1': 'một',
        '2': 'hai',
        '3': 'ba',
        '4': 'bốn',
        '5': 'năm',
        '6': 'sáu',
        '7': 'bảy',
        '8': 'tám',
        '9': 'chín'
    }
    
    num_str = str(number)
    
    text_list = [num_to_text[char] for char in num_str]
    text = ' '.join(text_list)
    
    return text

number = float(input("Nhập một số thập phân: "))
text = number_to_text(number)
print(number, "là", text)
