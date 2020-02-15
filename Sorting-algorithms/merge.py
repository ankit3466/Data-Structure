def merge_sort(arr):
    
    if len(arr)<=1:
        return arr
    mid = int(len(arr)/2)
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left,right)


def merge(left,right):

    i,j = 0,0
    result = []
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result += left[i:]
    result += right[j:]

    return result

array = [2,4,57,23,43,34,7,86,86,99,43,5,34,35,9089,423423,2343,4,765,7876,876]

print(merge_sort(array))
