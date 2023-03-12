import collections

def Find_max_second(a):
    max_1 = max(a[0], a[1])
    max_2 = min(a[0], a[1])

    for i in range(2, len(a)):
        if a[i] > max_1:
            max_2 = max_1
            max_1 = a[i]
        elif (a[i] > max_2) and (max_1 != a[i]):
            max_2 = a[i]

    return max_2

def check_duplicate_list(mylist):
    if len(mylist) != len(set(mylist)):
        return True
    else:
        return False

n = int(input("nhập số phần tử trong list: "))
lst = []
lst_location = []
count = 0
count_max = 0
if n == 1:
    print("số bạn nhập không đủ để so sánh")
else:
    for i in range(n):
        lst_input = int(input())
        lst.append(lst_input)

    max2 = Find_max_second(lst)
    max_list = max(lst)
    if check_duplicate_list(lst) == True:
        for i in lst:
            if i == max_list:
                count_max += 1

        if count_max > 1:
            for i in lst:
                if i == max_list:
                    lst.pop(lst.index(i))
                    new_max_2 = Find_max_second(lst)
                    lst.insert(lst.index(i),max_list - new_max_2 )
                    count_max -= 1
                break
            if count_max == 1:

                print("phần tử lớn thứ 2 trong danh sách là:", new_max_2)
                for i in lst:
                    if i == new_max_2:
                        count += 1
                    if count == 1:
                        for i in range(len(lst)):
                            if lst[i] == new_max_2:
                                print("vị trí của số lớn thứ 2 là: ",i+1)
                                break
                        break
                    else:
                        for i in lst:
                            if i == new_max_2:
                                lst_location.append(i)
                            else:
                                lst_location.append("no")
                        for j in range(len(lst_location)):
                            if lst_location[j] != "no":
                                print("vị trí của các số lớn thứ 2 là: ",j+1)
                    break

        else:
            for i in lst:
                if i == max2:
                    count += 1
                if count == 1:
                    for i in range(len(lst)):
                        if lst[i] == max2:
                            print("vị trí của số lớn thứ 2 là: ",i+1)
                            break
                else:
                    for i in lst:
                        if i == max2:
                            lst_location.append(i)
                        else:
                            lst_location.append("no")
                    for j in range(len(lst_location)):
                        if lst_location[j] != "no":
                            print("vị trí của các số lớn thứ 2 là: ",j+1)
                break

    else:
        for i in range(len(lst)):
            if lst[i] == max2:
                print("vị trí của số lớn thứ 2 là: ",i+1)
                break