def find_internal_nodes_num(tree):
    if len(tree) < 1:
        return 0
    unique_parents = set(tree)
    number_of_unique_parents = len(unique_parents)
    return number_of_unique_parents - 1


my_tree = [4, 4, 1, 5, -1, 4, 5]
print(find_internal_nodes_num(my_tree))

test_cases = []
test_cases.append([my_tree, 3])
test_cases.append([[-1, 0, 0, 0, 0, 1, 2, 2, 4, 5, 7], 6])
test_cases.append([[4, 3, 7, -1, 5, 3, 1, 1, 7, 1, 5], 5])
test_cases.append([[2, 12, 3, -1, 14, 6, 3, 13, 2, 14, 6, 10, 6, 10, 8, 8], 8])
test_cases.append([[], 0])
test_cases.append([[-1], 0])

for test_case in test_cases:
    assert find_internal_nodes_num(test_case[0]) == test_case[1]
