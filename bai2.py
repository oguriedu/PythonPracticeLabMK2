n = input("nhập vào số nguyên :") 
w = int(n) - 1
l = [] 
for i in range(w, 0, -1):  
  s = 0  
  for j in range(i,0, -1): 
    if i % j == 0 and j!= i:  
      s = s + j 
  if s == i: 
    l.append(i) 
print(l)