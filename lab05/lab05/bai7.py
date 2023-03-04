nhap=input("moi nhap: ")
van_ban="Xét tuyển theo kết quả Kỳ thi đánh giá tư duy do Đại học Bách khoa Hà Nội chủ trì tổ chức"
for i in list(van_ban.split()):
    if nhap == i:
        print((van_ban.split()).count(nhap))

      
