tuple_list = [('Alice', 25, 90), ('Bob', 30, 85), ('Charlie', 20, 95)]
sorted_tuple_list = sorted(tuple_list, key=lambda x: (x[0], x[1], x[2]))
print(sorted_tuple_list)
