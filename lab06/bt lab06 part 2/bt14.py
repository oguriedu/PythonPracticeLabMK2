a=[x for x in input("mời nhập mật khẩu: ").split(",")]
thuong=0
hoa=0
so=0
ky_tu=["$", "#","@" ]
while True:
  for i in a:
    tim1 = i.find(ky_tu[0])
    tim2 = i.find(ky_tu[1])
    tim3 = i.find(ky_tu[2])
    if len(i)>=6 and len(i)<=12:
        for k in i:
            if k.isnumeric():
                so+=1
            if k.islower():
                thuong+=1
            if k.isupper():
                hoa+=1 
        if so>=1 and thuong>=1 and hoa>=1 :
            if tim1>0 or tim2>0 or tim3>0:    
                print(i)
        break