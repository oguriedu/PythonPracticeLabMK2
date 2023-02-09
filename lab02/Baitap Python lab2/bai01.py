print("danh sách của các tháng: January, February, March, April, May, June, July, August, September, October, November, December")
tên_tháng = input("Nhập tên của tháng : ")

if tên_tháng == "February":
	print("số ngày là: 28/29 ngày")
elif tên_tháng in ("April", "June", "September", "November"):
	print("số ngày là : 30 ngày")
elif tên_tháng in ("January", "March", "May", "July", "August", "October", "December"):
	print("số ngày là: 31 day")
else:
	print("nhầm tên tháng") 