from unittest import result


numbers = [7, 17, 10, 5, 4, 3, 17, 5, 2, 5]
result = 0
n = int(input())

for fn in numbers:
    if fn == n :
        result += 1
print(result)