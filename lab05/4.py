str1 = input('Please enter the first string: ') 
str2 = input('Please enter the second string: ')

str3 = ''

for i in range(max(len(str1), len(str2))): 
    if i < len(str1): str3 += str1[i] 
    if i < len(str2): str3 += str2[i]

print(str3)