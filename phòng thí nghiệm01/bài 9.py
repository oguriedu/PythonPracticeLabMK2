x,y,z=map(float,input("tọa độ không gian OXYZ:").split())
x=int(input("X="))
y=int(input("Y="))
z=int(input("Z="))
OXY=x,y,-z
OXZ=x,-y,z
OYZ=-x,y,z
print("tọa độ OXY",OXY)
print("tọa độ OXZ",OXZ)
print("tọa độ OYZ",OYZ)
