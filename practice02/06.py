# 6.
import os
from random import random

low, high, cnt = 1, 100, 1
flag = True

while flag:
    os.system("clear")

    answer = int(random()*100)+1
    print("수를 결정하였습니다. 맞추어 보세요.")
    print("1-100")
    while flag:
        try:
            num = int(input("{}>>".format(cnt)))
        except ValueError:
            print("1-100까지의 정수를 입력해 주세요.")
            continue
        if num < answer:
            low = num
            print("더 높게")
            print("{}-{}".format(low, high))
            cnt += 1
            continue
        elif num > answer:
            high = num
            print("더 낮게")
            print("{}-{}".format(low, high))
            cnt += 1
            continue
        else:
            print("맞았습니다.")
            restrt = input("다시 하시겠습니까(y/n)>>")
            if restrt == 'n': flag = False
            else: break





