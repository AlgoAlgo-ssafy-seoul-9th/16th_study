# 병합정렬

def mergesort(lst):
    if len(lst) == 1:
        return lst

    mid = len(lst)//2
    l_lst = lst[:mid]
    r_lst = lst[mid:]

    l_lst = mergesort(l_lst)
    r_lst = mergesort(r_lst)

    merged_lst = []
    i, j = 0, 0
    L, R = len(l_lst), len(r_lst)

    while i < L and j < R:
        if l_lst[i] < r_lst[j]:
            merged_lst.append(l_lst[i])
            i += 1
        else:
            merged_lst.append(r_lst[j])
            j += 1

    
    while j != R:
        merged_lst.append(r_lst[j])
        j += 1

    while i != L:
        merged_lst.append(l_lst[i])
        i += 1

    return merged_lst

test = [4,5,1,3,2]
ans = mergesort(test)
print(ans)