ma = int ( input ( 'Nhập mã số sinh viên: ' ))
ho_ten = input ( 'Nhập tên họ: ' )
que = input ( 'Nhập quê quán: ' )
nam_sinh = int ( input ( 'Nhập năm sinh: ' ))
diem = float ( input ( 'Nhập điểm trung bình 3 môn: ' ))
print ( '{:<20}{:<20}{:<20}{:<12}{:<30}' . format ( 'Mã sinh viên' , 'Họ tên' , 'Quê quán' , 'Năm sinh' , 'Điểm trung bình 3 môn' ))
print ( '{:<20}{:<20}{:<20}{:<12}{:<30}' . định dạng ( ma , ho_ten , que , nam_sinh , diem ))