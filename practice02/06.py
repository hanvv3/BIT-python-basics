# 6.
import os
from random import random


while True:
    low, high, cnt = 1, 100, 1

    os.system("clear")
    answer = int(random()*100)+1
    print("수를 결정하였습니다. 맞추어 보세요.")

    while True:
        print("{}-{}".format(low, high))
        try:
            num = int(input("{}>>".format(cnt)))
        except ValueError:
            print("1-100까지의 정수를 입력해 주세요.")
            continue
        if answer == num:
            print("맞았습니다.")
            break
        if num < answer:
            low = num
            print("더 높게")
        else:
            high = num
            print("더 낮게")
        cnt += 1

    if 'n' == input("다시 하시겠습니까(y/n)>>"):
        break





