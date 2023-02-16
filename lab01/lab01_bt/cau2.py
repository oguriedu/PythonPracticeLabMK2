s = int (input('nhập số giây: '))
m = int (input ('nhập số phút: '))
h = int (input ('nhập số giờ: '))
d = int (input ('nhập số ngày: '))
doi = []
# đổi giây
second = s + m*60 + h*3600 + d*86400

# đổi phút
if s >=60:
    minute = (s//60) + m + h*60 + d*1140
else:
    minute =  m + h*60 + d*1140

# đổi giờ
if s >= 3600 and m >= 60:
    hours = (s//3600) + (m//60) + h + d*24
else:
    hours = h + d*24

# đổi ngày
if s >= 86400 and m >= 1140 and h >= 24:
    days = (s//86400) + (m//1140) + (h//24) + d
else:
    days = d

doi.append([second, minute, hours, days])
print(doi)