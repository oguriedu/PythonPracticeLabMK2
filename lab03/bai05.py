# Vẽ hình chữ nhật
 
c_dai = int(input("Nhập chiều dài HCN: "))
c_rong = int(input("Nhập chiều rộng HCN: "))
print("HÌNH CHỮ NHẬT")
for i in range(1, c_rong+1):
    for j in range(1, c_dai+1):
        print('* ', end='')
    print()