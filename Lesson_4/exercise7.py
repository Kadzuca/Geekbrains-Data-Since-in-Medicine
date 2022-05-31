from itertools import count
from math import factorial

def fact_gen():
    f_num = 1
    for i in count(1):
        yield factorial(i)

st = 0
for x in fact_gen():
    if st == 15:
        break
    else:
        st += 1
        print(str(st) + "=" + str(x))