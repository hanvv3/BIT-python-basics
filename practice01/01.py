# 1.

try:
    num = int(input("수를 입력하세요: "))
    if num % 3 == 0:
        print("3의 배수입니다.")
    else:
        print("3의 배수가 아닙니다.")
except ValueError:
    print("정수가 아닙니다.")
