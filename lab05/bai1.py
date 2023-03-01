'''
chương trình nhập chuỗi kí tự và đếm xem bao nhiêu kí tự là số
Program to input a string of characters and count how many characters are integer   
'''
n = input("nhập một chuỗi kí tự: ")
print("bạn vừa nhập: ", n)
n1 = 0
for i in n:
    if '0' <= i <= '9':
        n1 = n1 + 1
print("số các kí tự là số trong chuỗi là: ", n1)
