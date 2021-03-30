# 2.

try:
    num = int(input("수를 입력하세요 : "))
    if num % 2 == 0: print("짝수")
    else: print("홀수")
except ValueError:
    pass