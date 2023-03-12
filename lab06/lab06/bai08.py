n = int(input("Nhập vào số bất kỳ : "))
list_fibonacci = [0, 1]
[list_fibonacci.append(list_fibonacci[-1] + list_fibonacci[-2]) for i in range(n - 2)]
print("dãy finonaci ",",".join(str(f) for f in list_fibonacci))