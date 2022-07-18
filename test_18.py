word = 'banana'
my_dict = {}
for i in word:
    my_dict = {i}
    my_dict[i] = my_dict[i] + 1

    print(my_dict[i])