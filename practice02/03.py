# 3.

s = """We encourage everyone to contribute to Python. If you still have questions after reviewing the material in this guide, then the Python Mentors group is available to help guide new contributors through the process."""

s1 = s.replace('.', '')
s1 = s1.replace(',', '')
s1 = s1.replace('\n', '')
s1 = s1.upper().split(' ')

for i in s1:
    print(i)

for i in s1:
    print(i+':'+str(s1.count(i)))

