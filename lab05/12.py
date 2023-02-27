Str1 = input()
Str2 = input()
list_Str1 = []
list_Str2 = []
for i in range(1,len(Str1)):
    so_dau = int(Str1[:i])
    so_cuoi = int(Str1[i:])
    list_Str1.append([so_dau,so_cuoi]) 
for i in range(1,len(Str2)):
    so_dau = int(Str2[:i])
    so_cuoi = int(Str2[i:])
    list_Str2.append([so_dau,so_cuoi])
for i,j in zip(list_Str1,list_Str2):
    if i[0]+i[1]==j[0]+j[1]:
        print(f"{i[0]}+{i[1]}={j[0]}+{j[1]}")
        break
else:
    print('Không tồn tại cách đặt')
