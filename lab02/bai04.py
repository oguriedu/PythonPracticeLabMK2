'''Viết chương trình nhập 1 số nguyên, xuất ra chữ số hàng
trăm của số đó'''
n=int(input("Nhập 1 số nguyên: "))
def hang_tram(n):
    if n <= 99:
        print("0")
    else:
        m=str(n)
        print(m[-3])
hang_tram(n)