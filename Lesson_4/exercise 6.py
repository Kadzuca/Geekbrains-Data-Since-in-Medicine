from itertools import islice, cycle, count

def func(start_element, stop_element, num_str):
    try:
        start_element, stop_element, num_str = int(start_element), int(stop_element), int(num_str)
        check_list = [i for i in islice(count(), start_element, stop_element + 1)]
        repeat_list = [i for i in islice(cycle(check_list), num_str)]
        print(check_list)
        return repeat_list
    except ValueError:
        return "Error"

print(func(input("start: "), input("stop: "),input("number: ")))