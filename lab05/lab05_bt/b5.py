Str=input("Nhập chuỗi ký tự:")
sum=0
for i in Str:
    if "a" <=i<="z" or "A"<=i<="Z":
        del i
    else:
      if "1" <=i<="9":
          perfect_number=0
          sum*=0
          for j in range(len(i)):
             perfect_number+=int(i[j])
             for k in range(1,perfect_number):
                if perfect_number % k==0:
                        sum=sum+k
             if sum == perfect_number:
                    print(perfect_number,"là số hoàn hảo")
             else:
                    print(perfect_number,"không phải là số hoàn hảo")
                 
        