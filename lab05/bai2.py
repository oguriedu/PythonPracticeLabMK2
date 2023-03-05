str=input('mời nhập chuỗi kí tự:')
chu=0
for a in str:
      if a.isnumeric():
            chu+=1
print('số kí tự không phải chữ cái tiếng anh trong chuỗi vừa nhập là:',chu)
so=0
for b in str:
      if b.isalpha():
            so+=1
print('số kí tự không phải là số trong chuỗi vừa nhập là:',so)