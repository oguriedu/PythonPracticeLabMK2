password=[i for i in input("Nhập mk: ").split(",")]
point=0
for p in password:
    point=0
    if len(p)<6:
        continue
    for c in p:
        if c.isnumeric():
            if point>=1:
                continue
            point+=1          
        elif 'A'<=c<='Z':
            if point>=2:
                continue
            point+=1
        elif 'a'<=c<='z':
            if point>=3:
                continue
            point+=1
        else:
            if point>=4:
                continue
            point+=1
    if point==4:
        print("Đầu ra:",p[0:12])