
def bubble_sort(arr):

    x = len(arr)
    for i in range(0,x):
        for j in range(0,x-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]


array = [1,56,34,51,354,456,222222,131,46,868,7997]
bubble_sort(array)

print(array)


##################################################################


def bubble_sort(arr):

    x = len(arr)
    for i in range(x):

        swapped = False
        for j in range(0,x-1-i):

            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                swapped = True

        if swapped==False:
            break

array = [1,56,34,51,354,456,222222,131,46,868,7997]
bubble_sort(array)

print(array)

