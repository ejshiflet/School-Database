

import os
import loginControl


def checkForExistingInstructorFile():
    instructorFile = "instructor.csv"
    if not os.path.isfile(instructorFile):
        print("No Instructors have been added by an admin. Please contact an admin for a username and password.")
        quit()
    else:
        username = loginAndGetUserName()
    return username

def loginAndGetUserName():
    username = loginControl.login("instructor.csv","instructor")
    return username

#=====================================================================================================================================================


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

def listInstructors():#makes the file into a list
    courseInfo = []
    courseInstructors = []
    courseIndex = findColumnIndex("course.csv","instructorUsername")
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
            courseInstructors.append(number)
            i = i + 1
    return courseInstructors



def assignedCourses():
    info = listAllInfo("course.csv")
    allIntructorsInCourses = (listInstructors())
    countInstructors = allIntructorsInCourses.count(username)
    if countInstructors == 0:
        print("You are not assigned to teach any courses.")
        quit()
    else:
        print("Here are all the courses that you have been assigned: \n");
        for element in info:
            if element[2] == username:
                print("Course Number: " + element[0] + " | Course Title: " + element[1] + " | Instructor Username: " + element[2])
            

def listCourses():
    if not os.path.exists("course.csv"):
        print("You are not assigned to teach any courses.")
        while True:
            backToMainMenu = input("Type 1 and press enter to exit program -->")
            if backToMainMenu == "1":
                quit()
            else:
                print("Please enter the number 1 with no spaces")
    else:
        assignedCourses()

username = checkForExistingInstructorFile()
listCourses()
