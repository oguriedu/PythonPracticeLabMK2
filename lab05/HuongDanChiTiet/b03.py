S1 = input("Nhập chuỗi ký tự S1: ")
S2 = input("Nhập chuỗi ký tự S2: ")
vtc = S1.rfind(S2)
print("Vị trí xuất hiện sau cùng của chuỗi/xâu ký tự ",
      S2, " trong chuỗi ", S1, "là: %d" % vtc)
