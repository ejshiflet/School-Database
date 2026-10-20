


import os
import loginControl



def checkForExistingStudentsFile():
    studentFile = "student.csv"
    if not os.path.isfile(studentFile):
        print("No students have been added by an admin. Please contact an admin for a username and password.")
        quit()
    else:
        username = loginAndGetUserName()
    return username

def loginAndGetUserName():
    username = loginControl.login("student.csv","student")
    return username


#=====================================================================================================================================================

#enroll in course functions

def checkCourseFile():
    courseFile = "course.csv"
    if not os.path.isfile(courseFile):
        print("No courses have been created.")
        while True:
            backToMainMenu = input("Type 1 and press enter to return to main menu -->")
            if backToMainMenu == "1":
                displayMainMenu()
            else:
                print("Please enter the number 1 with no spaces")
    else:
        pass

def checkEnrollmentFile():
    enrollmentFile = "enrollment.csv"
    if not os.path.isfile(enrollmentFile):
        createStudentFile = open(enrollmentFile, "w")
        createStudentFile.write("courseNumber,studentUsername\n")
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

def findColumnIndex(fileName,columnName):# this will find the column
    info = loginControl.loginVerification(fileName)
    headers = info[0];
    i = 0;
    for element in headers:
        if element == columnName:
            break
        else:
            i = i + 1;
    return i;


def listCourseNumbers():#makes the file into a list
    courseInfo = []
    courseNumbers = []
    courseIndex = findColumnIndex("course.csv","number")
    i = 1
    openInstructorFile = open("course.csv", 'r'); 
    for element in openInstructorFile:
        newRow=element.split(',');
        newLastValue = newRow[len(newRow)-1];
        newRow[len(newRow)-1] = newLastValue[0:len(newLastValue)-1];
        courseInfo.append(newRow);
    for element in courseInfo:
        if i >= len(courseInfo):
            break
        else:
            number = courseInfo[i][courseIndex]
            courseNumbers.append(number)
            i = i + 1
    return courseNumbers

def getCourseChosen():
    allCourseInfo = listAllInfo("course.csv")
    courseNumbers = listCourseNumbers()
    print ("Here are the available classes: \n");
    j = 1;
    while j < len(allCourseInfo):
        print("Course Name: " + allCourseInfo[j][1] + " | Course Number: " + allCourseInfo[j][0] + " | Instructor Username: " + allCourseInfo[j][2])
        j = j + 1
    while True:
        instructorChosenInput = input("Type the course number here -->")  
        countInstructors = courseNumbers.count(instructorChosenInput)
        if countInstructors == 1:
            break
        print("Please enter the course number as shown with no spaces")
    return instructorChosenInput

def enrolledOrNot():
    enrollmentInfo = listAllInfo("enrollment.csv")
    studentUsername = username
    courseNumber = getCourseChosen()
    i = 0
    while i < len(enrollmentInfo):
        if enrollmentInfo[i][0] == courseNumber and enrollmentInfo[i][1] == studentUsername:
            print("You are already enrolled in this course.")
            while True:
                backToMenu = input('Enter "1" to go back to main menu.')
                if backToMenu == "1":
                    displayMainMenu()
                else:
                    print("Enter the number 1 with no spaces")
        else:
            i = i + 1
    return courseNumber

def enrollInCourse():
    global username
    checkCourseFile()
    checkEnrollmentFile()
    listAllInfo("course.csv")
    studentUsername = username
    chosenCourseNumber = enrolledOrNot()
    enrollmentInfo = (str(chosenCourseNumber) + "," + studentUsername + "\n")
    enrollmentFile = open("enrollment.csv","a")
    enrollmentFile.write(enrollmentInfo)
    enrollmentFile.close()
    print("\nEnrolled in course. Course information is shown below:\nYour Username: " + studentUsername + " | Course Number: " + chosenCourseNumber + "\n")
    while True:
        nextPage = input('Enter "1" to go back to main menu, "2" to exit the program, or "3" to continue adding courses -->')
        if nextPage == "1":
            displayMainMenu()
        elif nextPage == "2":
            quit()
        elif nextPage == "3":
            enrollInCourse()
        else:
            print("Enter the number 1, 2, or 3 with no spaces")

#=====================================================================================================================================================

#display enrolled courses functions

def enrolledCourses():
    info = listAllInfo("enrollment.csv")
    courses = []
    for element in info:
        if element[1] == username:
            courses.append(element[0])
    return courses
            
def makeEnrolledCoursesIntoString():
    allCourseInfo = listAllInfo("course.csv")
    studentEnrolledCourses = enrolledCourses()
    if studentEnrolledCourses ==  []:
        print("You have not enrolled in any courses.")
        while True:
            backToMainMenu = input("Type 1 and press enter to return to main menu -->")
            if backToMainMenu == "1":
                displayMainMenu()
            else:
                print("Please enter the number 1 with no spaces")
    else:
        print ("Here are all the courses you have enrolled in : \n");
        for element1 in studentEnrolledCourses:
            for element2 in allCourseInfo:
                if element1 == element2[0]:
                    print("Course Number: " + element2[0] + " | Course Title: " + element2[1] + " | Instructor Username: " + element2[2])         
        while True:
            backToMainMenu = input("Type 1 and press enter to return to main menu -->")
            if backToMainMenu == "1":
                displayMainMenu()
            else:
                print("Please enter the number 1 with no spaces")


def displayEnrolledCourses():
    if not os.path.exists("enrollment.csv"):
        print("You have not enrolled in any courses.")
        while True:
            backToMainMenu = input("Type 1 and press enter to return to main menu -->")
            if backToMainMenu == "1":
                displayMainMenu()
            else:
                print("Please enter the number 1 with no spaces")
    else:
        checkCourseFile()
        enrolledCourses()
        makeEnrolledCoursesIntoString()


#=====================================================================================================================================================


def displayMainMenu():
    print("\nWelcome to the main menu\n")
    print("Please enter the number next to the corresponding option:")
    print("1. Enroll in course\n2. See all course you are enrolled in\n3. Exit program and save\n")
    while True:
        menuOption = input("Enter the number with no spaces here then press enter -->")
        if menuOption == "1":
            enrollInCourse()

        elif menuOption == "2":
            displayEnrolledCourses()
          
        elif menuOption == "3":
            quit()

        else:
            print("Please enter a number between a number with no spaces 1 to 3.")


username = checkForExistingStudentsFile()
displayMainMenu()
