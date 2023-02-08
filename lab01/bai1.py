lst_ttsv=[]
def them_tt_sv(lst_ttsv):
      while True:
            ho_ten=input('Họ tên:')
            que_quan=input('Quê quán:')
            nam_snh=input('Năm sinh:')
            diem=float(input('Diểm trung bình cả năm:'))
            lst_ttsv.append({'ho_ten':ho_ten,'que_quan':que_quan,'nam_sinh':nam_snh,'diem':diem})
            return
them_tt_sv(lst_ttsv)


def in_ttsv(lst_ttsv):
     
      print('{:20}{:20}{:>20}{:>20}'.format('ho_ten','que_quan','nam_sinh','diem'))
      
      for sv in lst_ttsv:
            print('{:20}{:20}{:>20}{:>20}'.format(sv['ho_ten'], sv['que_quan'],sv['nam_sinh'],sv['diem']))

      return
in_ttsv(lst_ttsv)