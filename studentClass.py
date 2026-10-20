



class Student:
    #defines properties
    firstName = "";
    lastName = "";
    username = "";
    password = "";

    def __init__(sd,f,l,u,p):# constructor
        sd.firstName = f
        sd.lastName = l
        sd.username = u
        sd.password = p

    def __str__(sd):# makes string
        return "First Name: " + sd.firstName + "; Last Name: " + sd.lastName + "; Username: " + sd.username + "; Password: " + sd.password

#all setters

    def setFirstName(s, f):
        s.firstName = f;

    def setLastName(s,l):
        s.lastName = l;

    def setUsername(s,u):
        s.username = u;
    
    def setPassword(s,p):
        s.password = p;

#all getters

    def getFirstName(s):
        return s.firstName;

    def getLastName(s):
        return s.lastName;

    def getUsername(s):
        return s.username;

    def getPassword(s):
        return s.password;








