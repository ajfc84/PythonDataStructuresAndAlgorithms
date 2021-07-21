data = [10, 6, 2, 9, 4, 1]


def bubble_sort(my_list):
    for sink in range(len(my_list)-1):
        for current in range(len(my_list)-sink-1):
            if my_list[current] > my_list[current+1]:
                my_list[current], my_list[current+1] = my_list[current+1], my_list[current]
    return my_list


print(bubble_sort(data))

