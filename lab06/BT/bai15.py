from operator import itemgetter, attrgetter
I = []
while True:
    s = input()
    if not s:
        break
    I.append(tuple(s.split(',')))
print(sorted(I,key=itemgetter(0,1,2)))