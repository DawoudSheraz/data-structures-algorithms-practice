

def perform_delete(data_list, pt1, pt2):
    del data_list[pt1 + 1: pt2]
    return pt1 + 1, pt1 + 2


def remove_duplicates(data_list):
    pt1, pt2 = 0, 1

    while True:
        value1, value2 = data_list[pt1], data_list[pt2]
        if value1 == value2:
            pt2 += 1
        else:
            pt1, pt2 = perform_delete(data_list, pt1, pt2)
        if pt2 == len(data_list):
            break
    perform_delete(data_list, pt1, pt2)
    return data_list, len(data_list)


print(remove_duplicates([2, 3, 3, 3, 6, 9, 9, 10]))
print(remove_duplicates([2, 2, 2, 3, 4, 4, 6, 6, 9, 9, 9, 9, 11, 11, 12, 13, 14, 14, 14, 15, 16, 16, 16]))
