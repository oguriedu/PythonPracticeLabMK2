# initializing list
test_list = [(4, 5), (7, 6), (1, 0), (3, 4)]

# printing original list
print("The original list is : " + str(test_list))

# initializing search tuple
search_tup = [(3, 4), (8, 9), (7, 6), (1, 2)]

res = []
for i in search_tup:
    if i in test_list:
        res.append(test_list.index(i))

# printing result
print("The match tuple indices : " + str(res))
