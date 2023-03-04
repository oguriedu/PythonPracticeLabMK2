str1 = input()
str2 = input()
list_str1 = []
list_str2 = []
for i in range(1,len(str1)):
    so_dau = str1[:i]
    so_cuoi = str1[i:]
    list_str1.append([so_dau,so_cuoi]) 
for i in range(1,len(str2)):
    so_dau = str2[:i]
    so_cuoi = str2[i:]
    list_str2.append([so_dau,so_cuoi])
for i in list_str1:
    for j in list_str2:
      if int(i[0])+int(i[1])==int(j[0])+int(j[1]):
            print(f"{i[0]}+{i[1]}={j[0]}+{j[1]}")
            break
    else:
        continue
    break
else:
    print('Không tồn tại cách đặt')
