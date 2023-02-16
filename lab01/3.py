import math
def tinh(r,h):
    sday=r**2*math.pi 
    sxq=2*r*h*math.pi
    stp=2*r*math.pi*(r+h)
    v=sday*h
    if r<0 or h<0:
        print('bạn nhập không hợp lệ')
    else:
        print ("Dien tich day la:",sday)
        print('dien tich xung quanh',sxq)
        print('dien tich toan pha',stp)
        print('the tich',v)
if __name__=="__main__": 
    r=float(input("Nhap ban kinh: "))
    h=float(input("Nhap chieu cao: "))
    tinh(r,h)
    
