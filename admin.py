

import os
import loginControl


#=====================================================================================================================================================

# find column index for username and password functions


def findUsernameColumnIndex(fileName):# this will find the column
    loginInfo = loginControl.loginVerification(fileName)
    headers = loginInfo[0];
    i = 0;
    for element in headers:
        if element == "username":
            break
        else:
            i = i + 1;
    return i;

def findPasswordColumnIndex(fileName):# this will find the column
    loginInfo = loginControl.loginVerification(fileName)
    headers = loginInfo[0];
    i = 0;
    for element in headers:
        if element == "password":
            break
        else:
            i = i + 1;
    return i;

                

#=====================================================================================================================================================

#Add new student functions

def checkStudentFile():
    studentFile = "student.csv"
    if not os.path.isfile(studentFile):
        createStudentFile = open(studentFile, "w")
        createStudentFile.write("firstName,lastName,username,password\n")
    else:
        pass
        

def listStudentUsernames():#makes the file into a list
    studentInfo = []
    studentUsernames = []
    usernameIndex = findUsernameColumnIndex("student.csv")
    i = 1
    openStudentFile = open("student.csv", 'r'); #opens file in read mode
    for element in openStudentFile:
        newRow=element.split(',');
        newLastValue = newRow[len(newRow)-1];
        newRow[len(newRow)-1] = newLastValue[0:len(newLastValue)-1];
        studentInfo.append(newRow);
    for element in studentInfo:
        if i >= len(studentInfo):
            break
        else:
            username = studentInfo[i][usernameIndex]
            studentUsernames.append(username)
            i = i + 1
    return studentUsernames


def getStudentFirstName():
    studentFirstNameInput = input("\nEnter a student first name here -->")
    while not studentFirstNameInput.isalpha():# if the student name entered is not only letter the user will be asked to try again
        studentFirstNameInput = input("Please enter a first name with no spaces, numbers, or special characters -->");
    if studentFirstNameInput.isalpha():
        return studentFirstNameInput
    

def getStudentLastName():
    studentLastNameInput = input("Enter a student last name here -->"); # get student's last name
    while not studentLastNameInput.isalpha(): # if the student name entered is not only letter the user will be asked to try again
        studentLastNameInput = input("Please enter a last name with no spaces, number, or special characters -->");
    if studentLastNameInput.isalpha():
        return studentLastNameInput


def getStudentUsername():
    usernames = listStudentUsernames()
    while True:
        studentUsernameInput = input("Enter a student username here --> ")
        countUsername = usernames.count(studentUsernameInput)
        if not studentUsernameInput.isalnum():
            print("Enter a username with letters and numbers only")
            continue
        if countUsername == 0:
            break
        print("User name taken")
    return studentUsernameInput

def getStudentPassword():
    while True:
        studentPasswordInput = input("Enter a student password here --> ")
        if len(studentPasswordInput) > 24:
            print("Please enter a password under 25 characters -->")
            continue
        else:
            break
    return studentPasswordInput



def addNewStudent():
    checkStudentFile()
    listStudentUsernames()
    firstName = str(getStudentFirstName())
    lastName = str(getStudentLastName())
    username = str(getStudentUsername())
    password = str(getStudentPassword())
    newStudent = (firstName + "," + lastName + "," + username + "," + password + "\n")
    studentFile = open("student.csv","a")
    studentFile.write(newStudent)
    studentFile.close()
    print("\nNew student has been added. Student information is shown below:\nFirst Name: " + firstName + " | Last Name: " + lastName +  " | Username: " + username + " | Password: " + password + "\n")
    while True:
        nextPage = input('Enter "1" to go back to main menu, "2" to exit the program, or "3" to continue adding students -->')
        if nextPage == "1":
            displayMainMenu()
        elif nextPage == "2":
            quit()
        elif nextPage =="3":
            addNewStudent()
        else:
            print("Enter the number 1 or 2 with no spaces")
            

#=====================================================================================================================================================

#Add new intructor functions

def checkInstructorFile():
    instructorFile = "instructor.csv"
    if not os.path.isfile(instructorFile):
        createInstructorFile = open(instructorFile, "w")
        createInstructorFile.write("firstName,lastName,username,password,title\n")
    else:
        pass
        

def listInstructorUsernames():#makes the file into a list
    instructorInfo = []
    instructorUsernames = []
    usernameIndex = findUsernameColumnIndex("instructor.csv")
    i = 1
    openInstructorFile = open("instructor.csv", 'r'); #opens file in read mode
    for element in openInstructorFile:
        newRow=element.split(',');
        newLastValue = newRow[len(newRow)-1];
        newRow[len(newRow)-1] = newLastValue[0:len(newLastValue)-1];
        instructorInfo.append(newRow);
    for element in instructorInfo:
        if i >= len(instructorInfo):
            break
        else:
            username = instructorInfo[i][usernameIndex]
            instructorUsernames.append(username)
            i = i + 1
    return instructorUsernames


def getInstructorFirstName():
    instructorFirstNameInput = input("\nEnter an instructor first name here -->")
    while not instructorFirstNameInput.isalpha():# if the student name entered is not only letter the user will be asked to try again
        instructorFirstNameInput = input("Please enter a first name with no spaces, numbers, or special characters -->");
    if instructorFirstNameInput.isalpha():
        return instructorFirstNameInput
    

def getInstructorLastName():
    instructorLastNameInput = input("Enter an instructor last name here -->"); # get student's last name
    while not instructorLastNameInput.isalpha(): # if the student name entered is not only letter the user will be asked to try again
        instructorLastNameInput = input("Please enter a last name with no spaces, number, or special characters -->");
    if instructorLastNameInput.isalpha():
        return instructorLastNameInput
    
def getInstructorUsername():
    usernames = listInstructorUsernames()
    while True:
        instructorUsernameInput = input("Enter a instructor username here --> ")
        countUsername = usernames.count(instructorUsernameInput)
        if not instructorUsernameInput.isalnum():
            print("Enter a username with letters and numbers only")
            continue
        if countUsername == 0:
            break
        print("User name taken")
    return instructorUsernameInput

def getInstructorPassword():
    while True:
        instructorPasswordInput = input("Enter a instructor password here --> ")
        if len(instructorPasswordInput) > 24:
            print("Please enter a password under 25 characters -->")
            continue
        else:
            break
    return instructorPasswordInput

def getInstructorTitle():
    while True:
        instructorTitleInput = input('\nEnter the number next to the corresponding title name\n1. Assistant Professor\n2. Assosiate Professor\n3. Professor\nEnter the number with no space here -->')
        if instructorTitleInput == "1":
            return "Assistant Professor"
        elif instructorTitleInput == "2":
            return "Assosiate Professor"
        elif instructorTitleInput == "3":
            return "Professor"
        else: 
            print("\nPlease enter the number 1, 2, or 3\n")
            continue
        
def addNewInstructor():
    checkInstructorFile()
    listInstructorUsernames()
    firstName = str(getInstructorFirstName())
    lastName = str(getInstructorLastName())
    username = str(getInstructorUsername())
    password = str(getInstructorPassword())
    title = str(getInstructorTitle())
    newInstructor = (firstName + "," + lastName + "," + username + "," + password + "," + title + "\n")
    instructorFile = open("instructor.csv","a")
    instructorFile.write(newInstructor)
    instructorFile.close()
    print("\nNew Instructor has been added. Instructor information is shown below:\nFirst Name: " + firstName + " | Last Name: " + lastName +  " | Username: " + username + " | Password: " + password + " | Title: " + title +"\n")
    while True:
        nextPage = input('Enter "1" to go back to main menu, "2" to exit the program, or "3" to continue adding courses -->')
        if nextPage == "1":
            displayMainMenu()
        elif nextPage == "2":
            quit()
        elif nextPage == "3":
            addNewInstructor()
        else:
            print("Enter the number 1, 2, or 3 with no spaces")
            


#=====================================================================================================================================================

#Add new course functions

def checkForExistingInstructor():
    instructorFile = "instructor.csv"
    if not os.path.isfile(instructorFile):
        while True:
            backToMainMenu = input("You must add an instructor before creating a course. Type 1 and press enter to return to main menu -->")
            if backToMainMenu == "1":
                displayMainMenu()
            else:
                print("Please enter the number 1 with no spaces")
    else:
        pass


def checkCourseFile():
    courseFile = "course.csv"
    if not os.path.isfile(courseFile):
        createCourseFile = open(courseFile, "w")
        createCourseFile.write("number,title,instructorUsername\n")
    else:
        pass


def findCourseNumberColumnIndex(fileName):# this will find the column
    courseInfo = loginControl.loginVerification(fileName)
    headers = courseInfo[0];
    i = 0;
    for element in headers:
        if element == "number":
            break
        else:
            i = i + 1;
    return i;


def listCourseNumbers():#makes the file into a list
    courseInfo = []
    courseNumbers = []
    courseNumberIndex = findCourseNumberColumnIndex("course.csv")
    i = 1
    openCourseFile = open("course.csv", 'r'); #opens file in read mode
    for element in openCourseFile:
        newRow=element.split(',');
        newLastValue = newRow[len(newRow)-1];
        newRow[len(newRow)-1] = newLastValue[0:len(newLastValue)-1];
        courseInfo.append(newRow);
    for element in courseInfo:
        if i >= len(courseInfo):
            break
        else:
            courseNumber = courseInfo[i][courseNumberIndex]
            courseNumbers.append(courseNumber)
            i = i + 1
    return courseNumbers
        

def getCourseNumber():
    numbers = listCourseNumbers()
    while True:
        courseNumberInput = input("Enter a course number here --> ")
        countNumbers = numbers.count(courseNumberInput)
        if not courseNumberInput.isdigit():
            print("Enter a course number with numbers only")
            continue
        if countNumbers == 0:
            break
        print("Course number taken")
    return courseNumberInput

def getCourseTitle():
    courseTitleInput = input("Enter a course title here -->")
    while not courseTitleInput.isalpha():
        courseTitleInput = input("Please enter a course title with no spaces, numbers, or special characters -->");
    if courseTitleInput.isalpha():
        return courseTitleInput

def chooseInstructor():
    instructors = listInstructorUsernames()
    print("\nType an instructor username from the following list:")
    i = 1
    for element in instructors:
        print(str(i) + ". " + element)
        i = i + 1
    while True:
        instructorChosenInput = input("Type the instructor username here -->")  
        countInstructors = instructors.count(instructorChosenInput)
        if countInstructors == 1:
            break
        print("Please enter the instructor as shown with no spaces")
    return instructorChosenInput



def addNewCourse():
    checkForExistingInstructor()
    checkCourseFile()
    number = str(getCourseNumber())
    title = str(getCourseTitle())
    instructor = str(chooseInstructor())
    newCourse = (number + "," + title + "," + instructor + "\n")
    courseFile = open("course.csv","a")
    courseFile.write(newCourse)
    courseFile.close()
    print("\nNew course has been added. Course information is shown below:\nCourse Number: " + number + " | Course Title: " + title +  " | Course Instructor: " + instructor + "\n")
    while True:
        nextPage = input('Enter "1" to go back to main menu, "2" to exit the program, or "3" to continue adding courses -->')
        if nextPage == "1":
            displayMainMenu()
        elif nextPage == "2":
            quit()
        elif nextPage == "3":
            addNewCourse()
        else:
            print("Enter the number 1 or 2 with no spaces")
            


#=====================================================================================================================================================

#display all info general functions

def checkForAddedData(fileName,informationType):
    file = fileName
    if not os.path.isfile(file):
        while True:
            backToMainMenu = input("No " + informationType + " have been added. Type 1 and press enter to return to main menu -->")
            if backToMainMenu == "1":
                displayMainMenu()
            else:
                print("Please enter the number 1 with no spaces")
    else:
        pass

def listAllInfo(fileName):#makes the file into a list
    info = []
    openCourseFile = open(fileName, 'r'); #opens file in read mode
    for element in openCourseFile:
        newRow=element.split(',');
        newLastValue = newRow[len(newRow)-1];
        newRow[len(newRow)-1] = newLastValue[0:len(newLastValue)-1];
        info.append(newRow);
    return info

#=====================================================================================================================================================

#display all student info functions

def makeStudentInfoIntoString():
    allStudentInfo = listAllInfo("student.csv")
    print ("Here is the all the student information that has been entered: \n");
    j = 1;
    while j < len(allStudentInfo):
        print("First Name: " + allStudentInfo[j][0] + " | Last Name: " + allStudentInfo[j][1] + " | Username: " + allStudentInfo[j][2] + " | Password: " + allStudentInfo[j][3]);
        j = j + 1;
    while True:
            backToMainMenu = input("Type 1 and press enter to return to main menu -->")
            if backToMainMenu == "1":
                displayMainMenu()
            else:
                print("Please enter the number 1 with no spaces")

def displayAllStudentInfo(fileName):
    checkForAddedData("student.csv","students")
    listAllInfo(fileName)
    makeStudentInfoIntoString()


#=====================================================================================================================================================

#display instructor information functions

def makeInstructorInfoIntoString():
    allInstructorInfo = listAllInfo("instructor.csv")
    print ("Here is the all the instructor information that has been entered: \n");
    j = 1;
    while j < len(allInstructorInfo):
        print("First Name: " + allInstructorInfo[j][0] + " | Last Name: " + allInstructorInfo[j][1] + " | Username: " + allInstructorInfo[j][2] + " | Password: " + allInstructorInfo[j][3]  +  " | Title: " + allInstructorInfo[j][4]);
        j = j + 1;
    while True:
            backToMainMenu = input("Type 1 and press enter to return to main menu -->")
            if backToMainMenu == "1":
                displayMainMenu()
            else:
                print("Please enter the number 1 with no spaces")

def displayAllInstructorInfo(fileName):
    checkForAddedData("instructor.csv","instructors")
    listAllInfo(fileName)
    makeInstructorInfoIntoString()

#=====================================================================================================================================================

#display course information functions

def makeCourseInfoIntoString():
    allCourseInfo = listAllInfo("course.csv")
    print ("Here is the all the course information that has been entered: \n");
    j = 1;
    while j < len(allCourseInfo):
        print("Course Number: " + allCourseInfo[j][0] + " | Course Title: " + allCourseInfo[j][1] + " | Instructor Username: " + allCourseInfo[j][2])
        j = j + 1;
    while True:
            backToMainMenu = input("Type 1 and press enter to return to main menu -->")
            if backToMainMenu == "1":
                displayMainMenu()
            else:
                print("Please enter the number 1 with no spaces")

def displayAllCourseInfo(fileName):
    checkForAddedData("course.csv","courses")
    listAllInfo(fileName)
    makeCourseInfoIntoString()

#=====================================================================================================================================================

#display enrollment information functions
"""
def enrolledCourses():
    info = listAllInfo("enrollment.csv")
    courses = []
    theCourse = 
    for element in info:
        if element[1] == theCourse:
            courses.append(element[0])
    return courses

"""

def makeEnrollmentInfoIntoString():
    allEnrollmentInfo = listAllInfo("enrollment.csv")
    allCourseInfo = listAllInfo("course.csv")
    allInstructorInfo = listAllInfo("instructor.csv")
    allStudentInfo = listAllInfo("student.csv")
    print ("Here is the all the enrollment information that has been entered: \n");
    j = 1;
    while j < len(allEnrollmentInfo):
        course = allEnrollmentInfo[j][0]
        student = allEnrollmentInfo[j][1]
        for element1 in allCourseInfo:
            instructor = element1[2]
            if element1[0] == course:
                for element2 in allInstructorInfo:
                    if element2[2] == instructor:
                        for element3 in allStudentInfo:
                            if element3[2] == student:
                                print("Enrollment Info: " + str(j) + "\n\nCourse student is enrolled in info - Course Number: " + allEnrollmentInfo[j][0] +  " | Course Title: " + element1[1] + "\nInstructor of enrolled class info - Instructor: " + element1[2] + " | Instructor First Name: " + element2[0] + " | Instructor Last Name: " + element2[1] + "\nStudent enrolled in course info - Student Username: " + allEnrollmentInfo[j][1] + " | Student First Name: " + element3[0] + " | Student Last Name: " + element3[1] + "\n")
        j = j + 1;
    while True:
            backToMainMenu = input("Type 1 and press enter to return to main menu -->")
            if backToMainMenu == "1":
                displayMainMenu()
            else:
                print("Please enter the number 1 with no spaces")

def displayAllEnrollmentInfo(fileName):
    checkForAddedData("enrollment.csv","enrollments")
    listAllInfo(fileName)
    makeEnrollmentInfoIntoString()


#=====================================================================================================================================================
#display admin module mainmenu

def displayMainMenu():
    print("\nWelcome to the main menu\n")
    print("Please enter the number next to the corresponding option:")
    print("1. Add new student\n2. Add new instructor\n3. Add new course\n4. Show all student information\n5. Show all instructor information\n6. Show all course information\n7. Show all enrollment information\n8. Exit program and save\n")
    while True:
        menuOption = input("Enter the number with no spaces here then press enter -->")
        if menuOption == "1":
            addNewStudent()

        elif menuOption == "2":
            addNewInstructor()
          
        elif menuOption == "3":
            addNewCourse()
            
        elif menuOption == "4":
            displayAllStudentInfo("student.csv")
            
        elif menuOption == "5":
            displayAllInstructorInfo("instructor.csv")

        elif menuOption == "6":
           displayAllCourseInfo("course.csv")

        elif menuOption == "7":
            displayAllEnrollmentInfo("enrollment.csv")

        elif menuOption == "8":
            quit()
        
        else:
            print("Please enter a number between a number with no spaces 1 to 8.")

#=====================================================================================================================================================
        
loginControl.login("admin.csv","admin")
displayMainMenu()








    







