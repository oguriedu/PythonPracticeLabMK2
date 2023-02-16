import calendar
d=int(input("Enter day:"))
m=int(input('Enter month:'))
y=int(input("Enter year:"))
note1=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
print ("this day is ",note1[calendar.weekday(y,m,d)])