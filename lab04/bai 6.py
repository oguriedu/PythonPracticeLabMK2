a=['1','2','3','4','5','6','7','8','9']
b=['một','hai','ba','bốn','năm','sáu','bảy','tám','chín']
n=input('Nhập 1 số: ')
i=0
while i<=(len(n)-1):
    print(b[a.index(n[i])],end=' ')
    i+=1
