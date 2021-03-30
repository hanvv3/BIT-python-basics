# 9.

dic = {}

menu = input('메뉴: ')

if menu == '오뎅':
    dic['오뎅'] = 300
elif menu == '순대':
    dic['순대'] = 400
elif menu == '만두':
    dic['만두'] = 500
else:
    dic[menu] = 0

print("가격: {}".format(dic[menu]))
