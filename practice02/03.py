# 3.

s = """We encourage everyone to contribute to Python. If you still have questions after reviewing the material in this guide, then the Python Mentors group is available to help guide new contributors through the process."""

s1 = s.replace('.', '').replace(',', '').replace('\n', '')      # 함수를 한줄에 여러번 사용할 수 있다, (순서 주의)
s1 = s1.upper().split(' ')
s2 = list(set(s1))
s2.sort(key=str)                # key=str.lower을 사용하지만 이미 upper이기 때문에 str까지만 써줘도 상관없다.

for i in s1:
    print(i)

print()

for i in s2:
    print(i+':'+str(s1.count(i)))       # set()를 사용하면 중복을 지울수 있다.

    ################




