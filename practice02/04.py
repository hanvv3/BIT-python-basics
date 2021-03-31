# 4.

for i in range(1,100):
    num = str(i)
    flag = num.count('3') + num.count('6') + num.count('9')
    if flag > 0:
        print("{} ".format(num), end='')
        print("짝" * flag)





