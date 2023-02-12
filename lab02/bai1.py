x=float(input('nhập tháng(1 đến 12):'))
if x in [1,3,5,7,8,10,12]:
      print('Tháng',x,"có 31 ngày")
elif x in [4,6,9,11]:
      print('Tháng',x,'có 30 ngày')
elif x==2:
      print('Tháng 2 có 29 ngày')