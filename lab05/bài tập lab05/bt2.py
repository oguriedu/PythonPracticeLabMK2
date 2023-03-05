Srt = input("Nhập chuỗi kí tự:")
ta=0
so=0
for c in Srt:
    if "0"<=c<="9":
       so+=1
print("Chuỗi kí tự ko phải chữ cái :",so)
for c in Srt:
    if "a"<=c<="z"or"A"<=c<="Z":
       ta+=1
print("Chuỗi kí tự ko phải số:",ta)