# 병합정렬 연습
import sys
input = sys.stdin.readline


def merge_sort(start, end):
    # divide
    if end - start <= 1:
        return 
    mid = start + (end - start) // 2
    
    merge_sort(start, mid)
    merge_sort(mid, end)


    # conquer

    i,j = start, mid
    tmp = []
    while i< mid and j < end:
        if array[i] <= array[j]:
            tmp.append(array[i])
            i+=1
        else:
            tmp.append(array[j])
            j+=1
    while i < mid:
        tmp.append(array[i])
        i+=1
    while j < end:
        tmp.append(array[j])
        j+=1

    # combine
    for num in range(0, end-start):
        array[num+start] = tmp[num]
    
    return


if __name__ == "__main__":
    array = [4, 5, 1, 3, 2]
    merge_sort(0, len(array))
    print(array)