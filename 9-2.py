def my_range(first, last, step):
    number = first
    while (number < last):
        yield number
        number += step

c = my_range(0, 10, 1)

for i in c:
    print(i)