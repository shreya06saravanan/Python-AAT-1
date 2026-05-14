import pandas as pd
#Basic data of students
n=["John","Teressa","Micheal","Quincy","Issac","Richard","Julie"]
r1=[1,2,3,4,5,6,7]
m1=[38,35,47,43,29,31,41]
d=pd.DataFrame({"Name":n,"Roll_No":r1,"Marks":m1})

def menu():
    #Display Menu
    print("\n========== MENU ==========")
    print("1. Show all student details ")
    print("2. Show selective student details")
    print("3. Delete specific student")
    print("4. Delete all students")
    print("5. To view student details in order")
    print("6. Exit")
    global c
    c=int(input("Enter your choice: "))
def s1():
    #Display all student details
    for index, row in d.iterrows():
        print("Name:", row["Name"])
        print("Roll Number:", row["Roll_No"])
        print("Marks:", row["Marks"])
        print("-----------------------")
def s2():
    #Display selective student details
    print("\n Selected choice: Display selective student details:")
    print("Selection Menu")
    print("1. By Name")
    print("2. By Roll Number")
    print("3. By Marks")
    ch=int(input("Enter your choice: "))
    if ch==1:
        n=input("Enter the name of the student: ")
        result=d[d["Name"]==n]
        if not result.empty:
            print(result)
        else:
            print("Student not found.")
    elif ch==2:
        r=int(input("Enter the roll number of the student: "))
        result=d[d["Roll_No"]==r]
        if not result.empty:
            print(result)
        else:
            print("Student not found.")
    elif ch==3:
        m=int(input("Enter the marks of the student: "))
        result=d[d["Marks"]==m]
        if not result.empty:
            print(result)
        else:
            print("Student not found.")
def s3():
    #Delete specific student
    print("\n Selected choice: Delete specific student:")
    print("Selection Menu")
    print("1. By Name")
    print("2. By Roll Number")
    print("3. By Marks")
    ch=int(input("Enter your choice: "))
    if ch==1:
        n=input("Enter the name of the student to delete: ")
        w=d[d["Name"]!=n]
        print("Student with name", n, "has been deleted.")
    elif ch==2:
        r=int(input("Enter the roll number of the student to delete: "))
        w=d[d["Roll_No"]!=r]
        print("Student with roll number", r, "has been deleted.")
    elif ch==3:
        m=int(input("Enter the marks of the student to delete: "))
        w=d[d["Marks"]!=m]
        print("Student with marks", m, "has been deleted.")

def s4():
    #Delete all students
    print("\n Selected choice: Delete all students:")
    w=pd.DataFrame(columns=["Name","Roll_No","Marks"])
    print("All student records have been deleted.")
def s5():
    #View student details in order
    print("\n Selected choice: View student details in order:")
    print("Sorting Menu")
    print("1. By Name")
    print("2. By Roll Number")
    print("3. By Marks")
    ch=int(input("Enter your choice: "))
    if ch==1:
        sorted_d=d.sort_values(by="Name")
        print(sorted_d)
    elif ch==2:
        sorted_d=d.sort_values(by="Roll_No")
        print(sorted_d)
    elif ch==3:
        sorted_d=d.sort_values(by="Marks")
        print(sorted_d)
menu()
#Call the appropriate function based on user choice
if c==1:
    s1()
elif c==2:
    s2()
elif c==3:
    s3()
elif c==4:
    s4()
elif c==6:
    print("Exiting the program.")
elif c==5:
    s5()
else:
    print("Invalid choice.")
