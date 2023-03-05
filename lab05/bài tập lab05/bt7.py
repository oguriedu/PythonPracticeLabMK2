Str="""
Nam quốc sơn hà Nam đế cư

Tiệt nhiên phận định tại thiên thư

Như hà nghịch lỗ lai xâm phạm

Nhữ đẳng hành khan thủ bại hư
"""
tu=input('Nhập từ đơn cần tìm: ').lower()
lst=Str.lower().split()
count=0
for i in lst:
    if i == tu:
       count+=1 
print('Số từ đơn xuất hiện trong đoạn văn trên là: ',count)