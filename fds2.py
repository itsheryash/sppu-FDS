


def avg(list1):
    sum = 0
    count = 0
    for i in list1:
        
        sum += i
        count += 1
    avrage = sum/count
    print("\nAverage score of the class", avrage)


def maxmin(list1):
    for i in range(len(list1)):
        if list1[i] != 0:
            max = list1[i]
            for i in range(len(list1)):
                if list1[i] != 0:
                    if max < list1[i]:
                        max = list1[i]
    for i in range(len(list1)):
        if list1[i] != 0:
            min = list1[i]
            for i in range(len(list1)):
                if list1[i] != 0:
                    if min > list1[i]:
                        min = list1[i]
    print("Maximum score of the class", max)
    print("Minmum score of the class", min)


def absent(list1):
    count = 0
    for i in list1:
        if i == 0:
            count += 1
    print("Students absent for the test", count)

def maxFrequency(listofmarks):
    i = 0
    Max = 0
    print("Marks:Frequency")
    for j in listofmarks:
        if (listofmarks.index(j) == i):
            print(j, ":", listofmarks.count(j))
            if listofmarks.count(j) > Max:
                Max = listofmarks.count(j)
                mark = j
        i = i+1
    return(mark, Max)

Marks = [9, 8, 7, 6, 5, 4, 0]
# Marks=[]
# n=int(input("Enter number of students:"))
# print("Enter the marks of students if Absent Enter 0 \n")
# for i in range(n):
#     marks=int(input("Enter the marks of Roll Number"))
#     Marks.append(marks)
    

avg(Marks)
maxmin(Marks)
absent(Marks)
maxFrequency(Marks)
