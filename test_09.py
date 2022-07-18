from unittest import result


students = ['이영희', '김철수', '이영희', '조민지', '김철수', '조민지', '이영희', '이영희']
result = 0
for moon in students:
    if moon == '이영희':
        result += 1


print(result)
