# 5.

lst1 = [3, 6, 9, 12, 15, 18, 20, 32]
counts, Sum = 0, 0

for num in lst1:
    if num % 3 == 0:
        Sum += num
        counts += 1

print("주어진 리스트에서 3의 배수의 개수 => {}".format(counts))
print("주어진 리스트에서 3의 배수의 합 => {}".format(Sum))