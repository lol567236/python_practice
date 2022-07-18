a = int(input())
l = 0

while a > 0:
    a //= 10
    l += 1
print(l)