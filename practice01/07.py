# 7.

lst1 = []
Sum = 0

for i in range(5):
    num = int(input("정수 입력 : "))
    Sum += num
    lst1.append(num)
print("평균 : {}".format(Sum/len(lst1)))
