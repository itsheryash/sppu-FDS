def insertionsort(list1):
    for i in range(1, len(list1)):
        key = list1[i]
        j = i-1
        while j >= 0 and list1[j] > key:
            list1[j+1] = list1[j]
            j -= 1
        list1[j+1] = key

    print("insertion sort :", list1)

def shellsort(list1):

    interval = len(list1) // 2
    while interval > 0:
        for i in range(interval, len(list1)):
            temp = list1[i]
            j = i
            while j >= interval and list1[j - interval] > temp:
                list1[j] = list1[j - interval]
                j -= interval

            list1[j] = temp
        interval //= 2
    print("shell sort :", list1)

marks = [9, 5, 8, 7, 0, 3, 1, 4, 2]
print("unsorted list", marks)
insertionsort(marks)
shellsort(marks)