#chương trình tính xác xuất tung n lần 3 xúc xắc
# C=n!/(k!*(n-k)!)
#xác suất không tung ra cả 3 ra 6 lần nào:
n=int(input("nhập số lần tung"))
a=6*6*6#là tập nghiệm
# xác suất ít nhất 1 lần ra cả 3 xúc xắc là 6:
b=1
xac_suat=b/a
print("xác suất tung n lần 3 xúc xắc là : ",round(xac_suat**n,2))