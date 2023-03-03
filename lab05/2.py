length = 0 
for character in Str:
    if character not in "abcdefghijklmnopqrstuvwxyz" and character not in "0123456789": length += 1

print("There are " + str(length) + " non-alphanumeric characters in this string.")