from random import randint
some_list = [randint(-10, 10) for i in range(20)]
next_list = [i for i in some_list if some_list.count(i) == 1]
print(f'{some_list} \n {next_list}')