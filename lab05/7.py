Str="""
Cho trước xâu Str là một đoạn văn bản hoàn chỉnh ( có thể bao gồm nhiều dòng ). Nhập 
vào một từ đơn, hãy tìm trong chuỗi Str xem chứa bao nhiêu từ đơn này .
Ghi chú : từ đơn chính là từ chỉ có một âm tiết, hoặc một tiếng cấu tạo thành . Trong đó, âm 
tiết tiếng tạo nên từ đơn phải có nghĩa cụ thể khi đứng độc lập , riêng lẻ .
"""
find=input('Nhập từ đơn cần tìm: ').lower()
lst=Str.lower().split()
count=0
for i in lst:
    if i == find:
       count+=1 
print('Số từ đơn xuất hiện trong đoạn văn trên là: ',count)