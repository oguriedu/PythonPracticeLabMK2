a=input("nhập tọa độ điểm trên mặt phẳng oxyz (cách nhau bởi dấu ;): ")
t=a.split(";")
print("tọa độ điểm đối xứng qua oxy là ({},{},{})".format(int(t[0]),int(t[1]),-int(t[2])))
print("tọa độ điểm đối xứng qua oxz là ({},{},{})".format(int(t[0]),-int(t[1]),int(t[2])))
print("Tọa độ điểm đối xứng qua oyz là ({},{},{})".format(int(t[0]),int(t[1]),int(t[2])))