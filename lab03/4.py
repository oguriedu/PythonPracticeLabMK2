n = int(input("nhập một số "))
for i in range(2, n + 1):
  for j in range(2, i+1):
   if (i==j):
      print(i, "là số nguyên tố")
      break
   if (i % j) == 0:
    break
    