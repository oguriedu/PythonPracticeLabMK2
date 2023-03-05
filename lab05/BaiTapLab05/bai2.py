str="â123qweră456ưuơ789mnbchfjie"
print("Chuỗi ký tự : ",str)
count=0
for i in str:
    if "a"<=i<="z" or "0"<=i<="9" or "A"<=i<="Z":
        del i
    else:
        print(i,end=",")
        count+=1
print("\nCó",count,"ký tự không phải chữ cái tiếng Anh và không là số")
  