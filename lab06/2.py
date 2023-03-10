li=[]
while True:
    li.append(int(input('Nhập phần tử vào list:   ')))
    stop=input('Bạn muốn tiếp tục??(Nhập 0 để dừng lại):  ')
    if stop=='0':
        break
D=li.copy()
m=max(D)
i=0
while i<len(D):
    if D[i]==m:
        D.remove(D[i])
        i=1
    i+=1
if len(D)==0:
    print("Không có phần tử lớn thứ nhì")
else:
    m=max(D)
    print("Phần tử lớn thứ nhì là: ",m,"Vị trí của các phần tử đạt giá trị lớn nhì là: ",end="")
    for i in range(len(li)):
        if li[i]==m:
            print(i+1,end=",")
