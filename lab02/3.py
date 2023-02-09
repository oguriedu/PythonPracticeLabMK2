thu=['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
while True:
    a=int(input('Nhập thứ: '))
    if 0<a<8:
        break
    print('Không hợp lệ vui lòng nhập lại!')
print(f"{a}: {thu[a-1]}")
