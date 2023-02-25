s = input(" Nhập vào số cần tính tổng: ") 
total = 0 
i = 0 
while i<len(s): total += int(s[i]) 
i+=1

print("Tổng các chữ số của số nhập là:", total)