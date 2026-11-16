print("****Student Infomation****")
print("Student1,Student2,Student3,Student4,Student5")
def student1():
    print("Name:Jeehand\nAge:18\nCourse:Cyber")
def student2():
    print("Name:Nahil\nAge:18\nCourse:Python")    
def student3():
    print("Name:Haider\nAge:19\nCourse:DIT")
def student4():
    print("Name:Rahan\nAge:20\nCourse:CIT")
def student5():
    print("Name:Ibrahim\nAge:19\nCourse:Software Engenering")

user=input("enter which student infomation you needed:").upper()
if user=="1":
    student1()
elif user=="2":
    student2()   
elif user=="3":
    student3()
elif user=="4":
    student4()
elif user=="5":
    student5() 

elif user=="all":
    student1()
    student2()
    student3()
    student4()
    student5()

else:
    print("This Student is not found")