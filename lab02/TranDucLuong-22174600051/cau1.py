import calendar
y=int(input('Enter year:'))
m=int(input('Enter month:'))
x=calendar.monthrange(y,m)
x1=list(x)
print('Number of day:',x1[1])
