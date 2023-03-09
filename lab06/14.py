password=[i for i in input().split(",")]
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
        elif c.isalpha():
            if point>=2:
                continue
            point+=1
        else:
            if point>=3:
                continue
            point+=1
    if point==3:
        print(p[0:12])