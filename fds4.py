def selectionSort(list1):
    
    for i in range(len(list1)):
        min = i
        for j in range(i + 1, len(list1)):
            if list1[j] < list1[min]:
                min = j
        (list1[i], list1[min]) = (list1[min], list1[i])
    print("selection sort :", list1)
    
def bubblesort(list1):
    for i in range(len(list1)):
        for j in range(i+1, len(list1)):
            if list1[i]>list1[j]:
                list1[j],list1[i]=list1[i],list1[j]

marks=[9,5,8,7,0,3,1,4,2]
# marks=[]
# n=int(input("Enter marks you Want to add:"))
# for i in range(n):
#     m=int(input("Enter marks::"))
#     marks.append(m)
selectionSort(marks)
print(marks)
bubblesort(marks)
print(marks)

print("Top five marks are",marks[:-6:-1])