a = int(input("Nhập một số: "))
for i in range(2, a + 1):
  for j in range(2, i+1):
   if (i==j):
      print(i, "Là số nguyên tố")
      break
   if (i % j== 0):
    break