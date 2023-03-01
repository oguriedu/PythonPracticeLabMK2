alphabets = ["A", "B", "C", "D", "E", 'F', "G", "H", "I", "J", "K", "L",
             "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
numbers = [10, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 23,
           24, 25, 26, 27, 28, 29, 30, 31, 32, 34, 35, 36, 37, 38]

container_code = input("Enter code: ").upper()
if(len(container_code) != 10):
    print("Invalid code")
else:
    str_alphabets = container_code[:4]
    str_numbers = container_code[4:]
    if(str_alphabets.isalpha() and str_numbers.isnumeric()):
        total = 0
        index = 0
        for alphabet in str_alphabets:
            total = total + numbers[alphabets.index(alphabet)]*(2**index)
            ###
            print(
                f"{numbers[alphabets.index(alphabet)]}*2^{index} = {numbers[alphabets.index(alphabet)]*(2**index)}")
            ###
            index = index + 1
        for number in str_numbers:
            total = total + int(number)*(2**index)
            ###
            print(f"{int(number)}*2^{index} = {int(number)*(2**index)}")
            ###
            index = index+1
        print(total)
        print(f"Check digit: {total%11}")
    else:
        print("Invalid code")
