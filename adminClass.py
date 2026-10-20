
class Admin:
    #defines properties
    username = "";
    password = "";

    def __init__(ad,u,p):# constructor
        ad.username = u
        ad.password = p

    def __str__(ad):# makes string
        return "Username: " + ad.username + "; Password: " + ad.password

#all setters

    def setUsername(a,u):
        a.username = u;
    
    def setPassword(a,p):
        a.password = p;

#all getters

    def getUsername(a):
        return a.username;

    def getPassword(a):
        return a.password;


