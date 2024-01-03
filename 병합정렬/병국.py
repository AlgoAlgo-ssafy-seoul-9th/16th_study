arr = [4, 5, 1, 3, 2]


def merge_sort(arr):
    if len(arr) == 1:
        return arr

    mid = len(arr) // 2
    first = arr[0:mid]
    last = arr[mid:]

    first = merge_sort(first)
    last = merge_sort(last)
    answer_list = []

    i = j = 0
    
    # 비교
    while i < len(first) and j < len(last):
        if first[i] < last[j]:
            answer_list.append(first[i])
            i += 1
        else:
            answer_list.append(last[j])
            j += 1

    # 아직안들어간애 다넣어주고
    while i != len(first):
        answer_list.append(first[i])
        i += 1
    while j != len(last):
        answer_list.append(last[j])
        j += 1



    return answer_list


print(merge_sort(arr))