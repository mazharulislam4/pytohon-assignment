def find_out_duplicate(lst):
    duplicates = []

    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] == lst[j] and lst[i] not in duplicates:
                duplicates.append(lst[i])

    return duplicates


print(find_out_duplicate([1, 5, 6, 5, 1, 2, 3]))

#output [1 ,5]