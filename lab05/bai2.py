str=input("nhập chuỗi kí tự ban đâu = ")
print("chuỗi kí tự bạn vừa nhập là = ",str)
count=0
for c in str:
    if not("a"<=c<="z") and not("0"<=c<="9"):
        count+=1
print('số các kí tự cần tìm là ',count)