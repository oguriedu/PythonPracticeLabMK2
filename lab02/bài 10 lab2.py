start = int(input('nhập giờ bắt đầu: '))
end = int (input('nhập giờ kết thúc: '))
s = 0
hour = end - start

if start < 5 or start > 22 or end < 5 or end > 22:
    print ("thời gian không hợp lệ!!")
else:
    if hour >= 11 and hour <= 15:
        s += 100000 * (hour*0.9)
    elif hour > 3:
        s += 100000 * (hour*0.75)
    else:
        s += 100000 * hour
    print ('số tiền phải trả = ', s, 'VNĐ')

