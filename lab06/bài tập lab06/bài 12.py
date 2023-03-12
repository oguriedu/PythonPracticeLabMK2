sum = 0
while True:
    print("Choose the option numbers, 1:send to, 2:plug out,3: your money,4:exit ")
    n = int(input())
    if 1<= n and n <=4:
        if n == 1:
            send = int(input("How much money do you wanna send?: "))
            print("D: ",send)
            sum += send
        if n == 2:
            plug = int(input("How much money do you wanna plug?: "))
            print("W: ",plug)
            sum -= plug
            if plug > send:
                print("you not enough money!!!")
                break
        if n == 3:
            print("the total amount: ",sum)
        if n == 4:
            break
    else:   
        print("your number not correct! please re-enter: ")