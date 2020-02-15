
def selection_sort(arr):

    n = len(arr)
    for i in range(n):
        min_index = i

        for j in range(i+1,n):
            if arr[j]<arr[min_index]:
                min_index = j

        arr[i],arr[min_index] = arr[min_index],arr[i]



array = [232,4,2,13,343,556,5,765,558,345,2,12,2324,454,466,323,9]

selection_sort(array)
print(array)
