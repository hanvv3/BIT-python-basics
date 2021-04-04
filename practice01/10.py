# 10.

res = 0

num = int(input("숫자를 입력하세요: "))

i = num % 2
while i <= num:
    res += i
    i += 2
print("결과 값: {}".format(res))

################## 답안지 #####################

while True:
    number = input('숫자를 입력하세요:')
    if number.isdigit() is False:
        break

    number = int(number)

    s = 0
    for n in range(number+1):
        if number & 0x0001 ^ n & 0x0001 == 0:       # 연산순서: &(AND) 다음에 ^(XOR; 같으면0 다르면1)
            s += n                                  # 두 수가 서로 짝수나, 서로 홀수일 때 이 라인 실행.

    print('결과 값: {0}'.format(s))