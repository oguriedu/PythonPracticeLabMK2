#Tính tọa độ điểm đối xứng
x = int(input('Nhập x: '))
y = int(input('Nhập y: '))
z = int(input('Nhập z: '))
print("Tọa độ của điểm đối xứng với nó qua oxy là ({},{},{})".format(x,y,-z))
print("Tọa độ của điểm đối xứng với nó qua oxz là ({},{},{})".format(x,-y,z))
print("Tọa độ của điểm đối xứng với nó qua oyz là ({},{},{})".format(-x,y,z))