words = input()
w = list(words)
print(w)

for i in w:
    res = ord(i) - 64
    print(res , end = ' ')
    

