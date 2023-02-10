''' Viết chương trình nhập 1 số nguyên có 3 chữ số
in ra cách đọc của số đó'''
while True:
    n=int(input("Nhập số nguyên có 3 chữ số:"))
    def cach_doc(n):
        
        hang_tram=["Một trăm","Hai trăm","Ba trăm","Bốn trăm","Năm trăm","Sáu trăm","Bảy trăm","Tám trăm","Chín trăm",]
        hang_chuc=["linh","mười một","hai mươi","ba mươi","bốn mươi","năm mươi","sáu mươi","bảy mươi","tám mươi","chín mươi",]
        hang_donvi=["một","hai","ba","bốn","năm","sáu","bảy","tám","chín"]

        if 99<n<1000:
            m=str(n)
            print("Số",n,"đọc là:",hang_tram[int(m[-3])-1],hang_chuc[int(m[-2])],hang_donvi[int(m[-1])-1])
        else:
            print("Không hợp lệ nhập lại:") 
    cach_doc(n)