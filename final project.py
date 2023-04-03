class Course:
    id = 0
    def __init__(self,name,level):
        self.id = Course.id
        Course.id += 1
        self.name = name
        self.level = level

    def display_all(self):
        print(f"Course ID:{self.id}, Name:{self.name},course:{self.level} ")





class Student:
    id = 0
    def __init__(self,name,level):
        self.id = Student.id
        Student.id += 1
        self.name = name
        self.level = level
        self.course_list = []


    def make_course(self):
        new_course = str(input("Enter your course:"))
        if new_course != Course.Name:
           Course.Name.append(new_course)
        else:
            print(Course.Name)

    def display_all(self):
        print(f"Student ID:{self.id}, Name:{self.name},course:{self.course_list} ")




def print_StudentCourseMenu():
    print("Student Course Management System Menu:")
    print("Select an option:")
    print("1.Add new student")
    print("2.Remove student")
    print("3.Edit student")
    print("4.Display all students")
    print("5.Create new course")
    print("6.Display all courses")
    print("7.Add course to student")
    print("8.Exit")


student = []
course = []
course_list = []
while True:

    print_StudentCourseMenu()
    option = input("Please make a choice:")
    if option == "1":
        student_name = input("Enter student name:")
        student_level = input("Enter student level(A/B/C):")
        student_level = student_level.upper()
        while True:
            student_level = student_level.upper()
            if student_level not in ['A','B','C']:
                student_level = input("Invalid level, try again and enter student level(A/B/C):")
            else:
                print("student saved successfully")
                break
        std = Student(student_name, student_level )
        student.append(std)

    elif option == "2":
            ID = int(input("Enter student ID to remove:"))
            for i in student:
                if ID != i.id and i is student[-1]:
                    print("Student not found in the system")
                elif ID == i.id:
                    student.remove(i)
                    print(f"Student {i} has been removed from the system")

    elif option == "3":
        edit_ID = int(input("Enter student ID to edit:"))
        for i in student:
            if edit_ID != i.id and i is student[-1]:
                print("Student not found in the system")
            elif edit_ID == i.id:
                new_name = input("Enter new name")
                level_n = input("Enter new level")
                while True:
                  student_level = student_level.upper()
                  if student_level not in ['A', 'B', 'C']:
                      student_level = input("Invalid level, Enter student level(A/B/C):")
                  else:
                      i.name = new_name
                      i.level = level_n
                      print("student saved successfully")
                      break

                print("Student details updated successfully")


    elif option == "4":
        print("List of all students:")
        for i in student:
            i.display_all()


    elif option == "5":
        course_name = input("Enter course name:")
        course_level = input("Enter course level(A/B/C):")
        course_level = course_level.upper()
        while True:
            course_level = course_level.upper()
            if course_level not in ['A', 'B', 'C']:
                course_level = input("Invalid level, try again and enter course level(A/B/C):")
            else:
                print("course saved successfully")
                break
        cou = Course(course_name, course_level)
        course.append(cou)
        print("Course created successfully")
    elif option == "6":
        print("List of all courses:")
        for i in course:
            i.display_all()



    elif option == "7":
        id1 = int(input("Enter student ID:"))
        for i in student:
            if id1 != i.id and i is student[-1]:
                print("Student not found in the system. Try again!")
            elif id1 == i.id:
                id_course = int(input("Enter course ID:"))
                for a in course:
                    if id_course == i.id and a is course[-1]:
                        course_list.append(id_course)
                        print(f"Course {a.name} added to student {i.name}")

                    else:
                        print("Invalid course ID or course level does not match student le



    elif option == "8":
        print("Exit")
        break







