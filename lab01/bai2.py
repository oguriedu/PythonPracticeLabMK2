try:
    s=int(input('Số giây: '))
    if s>60:
        raise ValueError('Lỗi nhập thời gian !')
    if s<0:
        raise ValueError('Lỗi nhập thời gian !')
    m=int(input('Số phút: '))
    if m>60:
        raise ValueError('Lỗi nhập thời gian !')
    if m<0:
        raise ValueError('Lỗi nhập thời gian !')
    h=int(input('Số giờ: '))
    if h>24:
        raise ValueError('Lỗi nhập thời gian !')
    if h<0:
        raise ValueError('Lỗi nhập thời gian !')
    d=int(input('Số ngày: '))
    if d<0:
        raise ValueError('Lỗi nhập thời gian !')
except ValueError as ex:
    print(ex)
finally:
    print(d,' Ngày',h,' Giờ',m,' Phút',s,' Gây')