def longest_ascending_sequence(lst):
    if not lst:
        return []

    longest_sublist = []
    current_sublist = [lst[0]]

    for i in range(1, len(lst)):
        if lst[i] >= lst[i - 1]:
            current_sublist.append(lst[i])
        else:
            if len(current_sublist) > len(longest_sublist):
                longest_sublist = current_sublist
            current_sublist = [lst[i]]

    # Check at the end if the current sublist is the longest
    if len(current_sublist) > len(longest_sublist):
        longest_sublist = current_sublist

    return longest_sublist


# Test cases
print(longest_ascending_sequence([10, 70, 80, 20, 10, 10, 30, 50]))  # Expected: [10, 10, 30, 50]

lst = [0] * 1000
print(longest_ascending_sequence(lst))  # Expected: [0, 0, 0, ..., 0] (1000 zeros)

lst = [1, 2, 3, 4, 5, 6, 7, 8, 1, 2]
print(longest_ascending_sequence(lst))  # Expected: [1, 2, 3, 4, 5, 6, 7, 8]
