#Chương trình tính giá trị biểu thức
x=float(input("nhập giá trị x=: "))
f=(-x + sqrt(x**2+4))/(x**4+1)**(2/7)
print("phương trình có nghiệm là : %0.2f"%f)
