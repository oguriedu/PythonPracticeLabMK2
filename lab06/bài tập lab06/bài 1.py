a = [2,-4,1,9,-3,6,3,-2,6,8]
print(sum(a))
count = 0
sum = 0
for i in a:
    if i > 0:
        count += 1
        sum += i
print("number of positive elements: ",count)
print("sum of positive elements : ",sum)
for i in range(len(a)):
    if a[i] < 0:
        print("first negative element position: ",i + 1)
        break
for i in range(1,len(a)):
    if(a[-i] > 0):
        print("position of the last positive element: ",len(a) - i + 1)
        break
print("The largest element in the list is: ",max(a))
for i in range(len(a)):
    if a[i] == max(a):
        print("The position of the largest element in the list is: ",i+1)