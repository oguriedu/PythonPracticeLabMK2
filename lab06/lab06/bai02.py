lst=[]
n=int(input("nhap vao so n : "))
for i in range (0,n):
    num = int(input())
    lst.append(num)

print(lst)
mx = max(lst[0],lst[1])
n=len(lst)
for i in range (2,n):
    if lst[i] > mx :
        số_lớn_thứ_hai = mx
        mx = lst[i]
    elif lst[i] > số_lớn_thứ_hai and \
        mx !=lst[i] :
        số_lớn_thứ_hai = lst[i]
    elif mx == số_lớn_thứ_hai and \
        số_lớn_thứ_hai != lst[i]:
        số_lớn_thứ_hai = lst[i]

print("số lớn thứ hai trong list là :",\
      str(số_lớn_thứ_hai))
    