
def quick_sort(arr):

    if len(arr)<=1:
        return arr

    pivot = arr[0]
    lower,higher,equal = [],[],[]
    for x in arr:
        if x<pivot:
            lower.append(x)
        elif x==pivot:
            equal.append(x)
        else:
            higher.append(x)

    return quick_sort(lower)+equal+quick_sort(higher)


array = [22,1,1,2,34,4,345,645,675,68678,4534]

print(quick_sort(array))
