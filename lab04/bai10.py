dic = {1:'một',2:'hai',3:'ba',4:'bốn',5:'năm',6:'sáu',7:'bảy',8:'tám',9:'chín',0:'không'}
a = input('nhập một số:')
for i in a:
    if int(i) in dic:
        print(dic[int(i)],end=' ')