import random

s = [random.randint(1,9999) for i in range(10)]

# select_sort
for i in range(0, len(s) - 1):
    index = i
    print(index)
    for j in range(i + 1, len(s)):
        print(j)
        if s[index] > s[j]:
            index = j
    s[i], s[index] = s[index], s[i]

# print sort result.
print(s)