a=input("nhập văn bản: ")
b=input("nhập từ cần tìm: ")
try:
    print(f"{b} xuất hiện {a.count(b)} lần trong văn bản trên")
except:
    print(f"{b} không có trong {a}")
