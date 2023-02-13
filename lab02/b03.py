a, b, c = map(float, input('Nhập độ dài các cạnh: ').split(","))
if a+b < c or b+c < a or c+a < b:
    print('Không phải là độ dài 3 cạnh của tam giác ')
elif a == b or a == c or b == c:
    if a == b == c:
        print('Đây là tam giác đều')
    elif a*a == b*b+c*c or b*b == a*a+c*c or c*c == a*a+b*b:
        print('Đây là tam giác vuông cân!')
    else:
        print('Đây là tam giác cân')
elif a*a == b*b+c*c or b*b == a*a+c*c or c*c == a*a+b*b:
    print('Đây là tam giác vuông')
else:
    print('Đây là tam giác thường.')
