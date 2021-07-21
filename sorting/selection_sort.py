def selection_sort(my_list):
    for i in range(len(my_list)):
        min_index = i
        for j in range(i+1, len(my_list)):
            if my_list[min_index] > my_list[j]:
                min_index = j
            my_list[min_index], my_list[i] = my_list[i], my_list[min_index]
    return my_list


data = [1, 5, 3, 2, 9, 10]
print(selection_sort(data))