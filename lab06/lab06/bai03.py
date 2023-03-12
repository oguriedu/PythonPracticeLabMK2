lst_số=[]
lst1=[]
while True:
        n=int(input("nhập vào số :"))
        lst_số.append(n)
        if n==0: 
            print("sai giá trị ")
        break
print("lst số mà bạn đã nhập là :",lst_số)
#a
lst1=lst_số.copy()
lst1.sort(reverse=True)
print("list sắp xếp lại là :",lst1)
#b
w=int(input("nhập vào phần tử cần chèn :"))
lst_số.append(w)
lst_số.insert(5,w)
lst_số.insert(0,w)
print(f"phần tử chèn vào list là {lst_số}")