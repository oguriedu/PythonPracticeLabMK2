s=input("nhập chuỗi ký tự s: ")
s1=input("nhập chuỗi ký tự s1: ")
n=len(s)
for i in range(1,1+n ,1):
    s1+=s[len(s)-i]
print("chuỗi ký tự nghịch đảo của ",s," là: ",s1)