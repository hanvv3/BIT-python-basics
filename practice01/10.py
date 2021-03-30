# 10.

res = 0

num = int(input("숫자를 입력하세요: "))

i = num % 2
while i <= num:
    res += i
    i += 2
print("결과 값: {}".format(res))
