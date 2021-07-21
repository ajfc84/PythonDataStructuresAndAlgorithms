def insertion_sort(my_list):
    for i in range(1, len(my_list)):
        key = my_list[i]
        j = i-1
        while j >= 0 and key < my_list[j]:
            my_list[j+1] = my_list[j]
            j -= 1
        my_list[j+1] = key
    return my_list


data = [2, 1, 7, 6, 5, 3, 4, 9, 8]
print(insertion_sort(data))

