# 2.

try:
    num = int(input("수를 입력하세요 : "))
    if num % 2 == 0: print("짝수")
    else: print("홀수")
except ValueError:
    pass

print('짝수' if int(num) & 0x0001 == 0 else '홀수')     # 이렇게도 사용가능

