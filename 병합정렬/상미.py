## 병합정렬
## [4, 5, 1, 3, 2]

def merge_sort(lst):
    if len(lst) > 1:
        mid = len(lst) // 2
        left = lst[:mid]
        right = lst[mid:]

        merge_sort(left)
        merge_sort(right)

        i, j, tmp = 0, 0, 0
        
        # 양쪽 리스트 비교
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                lst[tmp] = left[i]
                i += 1
            else:
                lst[tmp] = right[j]
                j += 1
            tmp += 1
        # 왼쪽만 남으면
        while i < len(left):
            lst[tmp] = left[i]
            i += 1
            tmp += 1
        # 오른쪽만 남으면
        while j < len(right):
            lst[tmp] = right[j]
            j += 1
            tmp += 1
    return lst

lst = [4, 5, 1, 3, 2]
print(merge_sort(lst))