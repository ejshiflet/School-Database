


class Instructor:
    #defines properties
    firstName = "";
    lastName = "";
    username = "";
    password = "";
    title = "";

    def __init__(it,f,l,u,p,t):# constructor
        it.firstName = f
        it.lastName = l
        it.username = u
        it.password = p
        it.title = t
        
    def __str__(it):# makes string
        return "First Name: " + it.firstName + "; Last Name: " + it.lastName + "; Username: " + it.username + "; Password: " + it.password + ";Title: " + it.title

#all setters

    def setFirstName(i, f):
        i.firstName = f;

    def setLastName(i,l):
        i.lastName = l;

    def setUsername(i,u):
        i.username = u;
    
    def setPassword(i,p):
        i.password = p;
    
    def setTitle(i,t):
        i.title = t;

#all getters

    def getFirstName(i):
        return i.firstName;

    def getLastName(i):
        return i.lastName;

    def getUsername(i):
        return i.username;

    def getPassword(i):
        return i.password;

    def getTitle(i):
        return i.title;









