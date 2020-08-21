lst = [8, 2, 6, 4, 3, 1]


def condition(x):
    return 7 > x > 1


filtered = [x for x in lst if condition(x)]
print(filtered)

filtered = filter(lambda x: x < 6, lst)
print(list(filtered))
