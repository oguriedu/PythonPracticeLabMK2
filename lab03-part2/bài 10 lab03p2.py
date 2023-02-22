number = int (input('nhập số nguyên dương n: '))
def pt_thua_so_ngto(n):
    i = 2
    list_number = []
    while i*i <= n:
        if n % i:
            i+=1
        else:
            n //= i
            list_number.append(i)
    if n > 1:
        list_number.append(i)
    return list_number
print('Dạng phân tích thừa số của số nguyên dương', number, '=', pt_thua_so_ngto(number))
