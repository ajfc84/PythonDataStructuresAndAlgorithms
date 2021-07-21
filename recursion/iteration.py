def iteration(array, i):
    if i <= 0:
        return None
    else:
        iteration(array, i-1)
        print(array[i-1])


iteration("hello", len("hello"))


def iteration2(array):
    if len(array) <= 0:
        return None
    else:
        iteration2(array[:-1])
        print(array[-1])


iteration2("hello")

