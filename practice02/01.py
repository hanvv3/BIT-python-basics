# 1.

s = '/usr/local/bin/python'

lst = s[1:].split('/')
r = ','.join(lst)
print(r)

# print(s.)
r = ','.join(s.rsplit('/', 1))       # 1은 개수, ','.join으로 묶어줌
print(r)
