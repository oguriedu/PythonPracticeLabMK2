print('Nhập ký tự :', end='')
ky_tu = input()
if ky_tu == 'O' or ky_tu == 'o' or\
   ky_tu == 'U' or ky_tu == 'u' or\
   ky_tu == 'I' or ky_tu == 'i' or\
   ky_tu == 'A' or ky_tu == 'a' or\
   ky_tu == 'E' or ky_tu == 'e':
    print("Ký tự '", ky_tu, "' là nguyên âm!")
else:
    print("Ký tự '", ky_tu, "' là phụ âm!")
