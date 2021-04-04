# 6.

cash = int(input("금액 입력 : "))
res = cash

print("금액 : {}".format(cash))
print()
if res // 50000 > 0:
    print("50000원 : {}개".format(res//50000))
    res -= 50000*(cash//50000)
if res // 10000 > 0:
    print("10000원 : {}개".format(res//10000))
    res -= 10000*(res//10000)
if res // 5000 > 0:
    print("5000원 : {}개".format(res//5000))
    res -= 5000*(res // 5000)
if res // 1000 > 0:
    print("1000원 : {}개".format(res//1000))
    res -= 1000*(res // 1000)
if res // 500 > 0:
    print("500원 : {}개".format(res//500))
    res -= 500*(res // 500)
if res // 100 > 0:
    print("100원 : {}개".format(res//100))
    res -= 100*(res // 100)
if res // 50 > 0:
    print("50원 : {}개".format(res//50))
    res -= 50*(res // 50)
if res // 10 > 0:
    print("10원 : {}개".format(res//10))
    res -= 10*(res // 10)
if res // 5 > 0:
    print("5원 : {}개".format(res//5))
    res -= 5*(res // 5)
if res > 0:
    print("1원 : {}개".format(res))


cash = int(cash)
for won in [50000, 10000, 5000, 1000, 500, 100, 50, 10, 50, 1]:
    count = cash // won
    cash -= count*won
    print('{0}원: {1}개'.format(won, count))
