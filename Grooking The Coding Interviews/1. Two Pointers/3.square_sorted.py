

def square_sorted(input_array):
    output = []
    pt1, pt2 = 0, len(input_array) - 1

    while len(output) != len(input_array):
        sq1 = input_array[pt1] ** 2
        sq2 = input_array[pt2] ** 2
        if sq1 > sq2:
            pt1 += 1
            output.insert(0, sq1)
        else:
            pt2 -= 1
            output.insert(0, sq2)
    return output


print(square_sorted([-2, -1, 0, 2, 3]))
print(square_sorted([-3, -1, 0, 1, 2]))
