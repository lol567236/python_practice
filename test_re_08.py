number_list = [1, 23, 9, 6, 91, 59, 29 , 2]
max1 = max(number_list)
print(max1)



number_list2 = [2, 5, 100, 20, 50, 10, 91, 82]

max2 = max(number_list2)
print(max2)

if max1 > max2:
    print("첫 번째 리스트의 최댓값이 더 큽니다.")

elif max1 < max2:
    print("두 번째 리스트의 최댓값이 더 큽니다.")

else:
    print("첫 번째 리스트의 최댓값과 두 번째 리스트의 최댓값은 같습니다.")