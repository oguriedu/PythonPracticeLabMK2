#chương trình nhập vào số nguyên 3 chữ số
cac_hang=["mươi","mốt","hai","ba","bốn","năm","sáu","bảy","tám","chín"]
nhap=int(input('nhập vào số nguyên 3 chữ số: '))
hang_tram=nhap//100
hang_chuc=(nhap%100)//10
hang_don_vi=(nhap%100)%10
doc1=0
doc2=0
doc3=0
cac_hang2=["một","hai","ba","bốn","năm","sáu","bảy","tám","chín"]
if hang_don_vi==0 and hang_don_vi!=1:
    for i in range(0,len(cac_hang)+1):
        if hang_chuc==i:
            doc2=cac_hang[i]
        if hang_don_vi==i:
            doc3=cac_hang[i]
        if hang_tram==i:
            doc1=cac_hang[i]
elif hang_don_vi!=0 and hang_tram==1:
    for i in range(0,len(cac_hang2)+1):
        if hang_tram==i:
            doc1=cac_hang[i-1]
        if hang_chuc==i:
            doc2=cac_hang2[i-1]+" "+str("mươi")
        if hang_don_vi==i:
            doc3=cac_hang2[i-1]


print(doc1,"trăm",doc2,doc3)