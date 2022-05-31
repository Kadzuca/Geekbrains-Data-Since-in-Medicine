some_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
more_list = [some_list[i] for i in range(1, len(some_list)) if some_list[i] > some_list[i - 1]]
print(more_list)