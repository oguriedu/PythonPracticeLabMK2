S = input("Nhập chuỗi ký tự S: ")
S1 = ''
n = len(S)
for i in range(1, n+1, 1):
    S1 += S[len(S)-i]
print("Chuỗi ký tự nghịch đảo của '", S, "' là: '", S1, "'")
