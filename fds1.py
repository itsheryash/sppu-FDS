
def cb(list1,list2):
    listcb=[]
    for i in list1:
        if i in list2:
            listcb.append(i)
    print("\nStudents who play Cricket and Badminton",listcb)
    return listcb

def cf(list1,list2):
    listcf=[]
    for i in list1:
        if i in list2:
            listcf.append(i)
    print("\nStudents who play Cricket and Football",listcf)
    return listcf

def nCnB(Allstudents,C,B):
    nCB=[]
    for i in Allstudents:
        if i not in C and i not in B:
            nCB.append(i)
    print("\nStudents who play neither Cricket nor Badminton",nCB)
    return nCB

def eCrB(list1,list2):
    eCB=[]
    for i in list1:
        if i not in list2:
            eCB.append(i)
    
    for i in list2:
        if i not in list1:
            eCB.append(i)
    print("\nStudents who play either Cricket or Badminton but not both",eCB)


# students=["A","B","C","D","E"]
# cricket=["A","B"]
# Badminton=["C","D","A"]
# football=["B","E"]
students=[]
cricket=[]
Badminton=[]
football=[]

n=int(input("Enter the number of students in SE:"))
for i in range(n):
    name=input("enter the name of students:")
    students.append(name)


nC=int(input("\nEnter the Number of Students who play Cricket:"))
for i in range(nC):
    name=input("Enter the Name of Students:")
    cricket.append(name)


nB=int(input("\nEnter the Number of Students who play Badminton:"))
for i in range(nB):
    name=input("Enter the Name of Students:")
    Badminton.append(name)


nF=int(input("\nEnter the Number of Students who play Football:"))
for i in range(nF):
    name=input("Enter the Name of Students:")
    football.append(name)


cb(cricket,Badminton)
cf(cricket,football)
nCnB(students,cricket,Badminton)
eCrB(cricket,Badminton)