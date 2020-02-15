
def insertion_sort(arr):

    n = len(arr)
    for i in range(1,n):

        key = arr[i]
        j=i-1
        while j>=0 and key<arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1]=key

array = [34,2,1,3,4,5435,46,657,65,86,684,32,24,44,7,34,324]

insertion_sort(array)
print(array)
