chungu = ["Anh","Em"]
dongtu = ["Chơi","Yêu"]
tanngu = ["Bóng đá","Xếp hình"]
for i in range(len(chungu)):
    for j in range(len(dongtu)):
        for l in range(len(tanngu)):
            thanhcau = "%s%s%s"%(chungu[i],dongtu[j],tanngu[l])
            print(thanhcau)