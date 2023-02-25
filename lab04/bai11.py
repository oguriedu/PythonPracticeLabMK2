while True:
      print("MENU")
      print('1.Cafe')
      print('2.Nước ép cà rốt')
      print('3.Nước lọc ')
      print('4.Nước dừa ')


      a=int(input('Vui lòng chọn loại nước '))
      if a==1:
            print('Cafe')
      elif a==2:
            print('Nước ếp cà rốt')
      elif a==3:
            print('Nước lọc')
      elif a==4:
            print("Nước dừa")
      else:
            print('Vui lòng chọn lại 1 trong 4 loại nước trên')
                 
      tt=input('nhấn phím bất kì đẻ tiếp tục(nhấn 0 để dừng lại)')
      if tt=='0':
            break
