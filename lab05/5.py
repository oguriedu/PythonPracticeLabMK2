new_str = "" 
for char in str: 
    if char.isdigit(): new_str += char

print(f"The new string is {new_str}")

if int(new_str) > 0 and sum(list(map(int, str(new_str)))) == 0: print("This is a perfect number.") 
else: print("This is not a perfect number.")