

def pair(data_list, target):
    left = 0
    right = len(data_list) - 1
    while True:
        current_sum = data_list[left] + data_list[right]
        if current_sum == target:
            return left, right, data_list[left], data_list[right]
        if current_sum < target:
            left += 1
        if current_sum > target:
            right -= 1


def pair_hash_map(data_list, target):
    seen = {}
    for idx, item in enumerate(data_list):
        value = target - item
        if value in seen:
            return seen[value], idx, value, item
        else:
            seen[item] = idx


print(pair_hash_map([1, 2, 3, 4, 6], 6))
print(pair([1, 2, 3, 4, 6], 6))
print(pair_hash_map([2, 5, 9, 11], 11))
print(pair([2, 5, 9, 11], 11))
