S = ['Anh','Em']
V = ['Chơi','Yêu']
O = ['Bóng đá','Sếp hình']
for i in range(len(S)):
    for j in range(len(V)):
        for h in range(len(O)):
            cau ='%s %s %s' % (S[i],V[j],O[h])
            print(cau)