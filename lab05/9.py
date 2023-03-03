def LongestCommonSubstring( str1, str2): lcs_array = [[0 for x in range(len(str2)+1)] for x in range(len(str1)+1)] 
longest_length = 0 
longest_end = 0 
for i in range(len(str1)): 
    for j in range(len(str2)): 
        if str1[i] == str2[j]: lcs_array[i+1][j+1] = lcs_array[i][j] + 1 
        if lcs_array[i+1][j+1] > longest_length: longest_length = lcs_array[i+1][j+1] 
        longest_end = i+1 
        return str1[longest_end - longest_length: longest_end]

str1 = input("Nhập chuỗi str1: ") 
str2 = input("Nhập chuỗi str2: ")

print("Chuỗi con chung của 2 chuỗi có độ dài cực đại là:", LongestCommonSubstring(str1, str2))