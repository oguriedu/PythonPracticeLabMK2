Str1=input()
max_len = 0
max_str = "" 
cur_len = 0 
cur_str = "" 
cur_char = ""
for c in Str1:
    if c == cur_char:
      cur_len += 1
      cur_str += c
    else:
        cur_char = c
        if cur_len > max_len: 
            max_len = cur_len 
            max_str = cur_str  
        cur_len = 1 
        cur_str = c 
if cur_len > max_len: 
    max_len = cur_len 
    max_str = cur_str 
print(max_str)