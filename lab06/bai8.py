n = int(input("Nhập số n : "))
fibonacci = [0, 1]
[fibonacci.append(fibonacci[-1] + fibonacci[-2]) for i in range(n - 2)]
print("dãy finonaci ",",".join(str(f) for f in fibonacci))
