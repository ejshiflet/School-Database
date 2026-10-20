
from instructorClass import Instructor

class Course:
    #defines properties
    number = "";
    title = "";
    instructor = Instructor()

    def __init__(co,n,t,i):# constructor
        co.number = n
        co.title = t
        co.instructor = i

    def __str__(co):# makes string
        return "Number: " + co.number + "; Title: " + co.title +  "; Instructor: " + str(co.instructor)


#all setters

    def setNumber(c,n):
        c.number = n;
    
    def setTitle(c,t):
        c.title = t;

#all getters

    def getNumber(c):
        return c.number;

    def getPassword(c):
        return c.title;


