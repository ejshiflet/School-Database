







def loginVerification(fileName):#makes the file into a list
    loginInfo = []
    loginInfoFile = open(fileName, 'r'); #opens file in read mode
    for x in loginInfoFile:
        newRow=x.split(',');
        newLastValue = newRow[len(newRow)-1];
        newRow[len(newRow)-1] = newLastValue[0:len(newLastValue)-1];
        loginInfo.append(newRow);
    return loginInfo


def findUsernameColumnIndex(fileName):# this will find the column
    loginInfo = loginVerification(fileName)
    headers = loginInfo[0];
    i = 0;
    for element in headers:
        if element == "username":
            break
        else:
            i = i + 1;
    return i;

def findPasswordColumnIndex(fileName):# this will find the column
    loginInfo = loginVerification(fileName)
    headers = loginInfo[0];
    i = 0;
    for element in headers:
        if element == "password":
            break
        else:
            i = i + 1;
    return i;

def checkLoginInfo (usernameIndex, passwordIndex,list,moduleName):
    doneOrNot = ""
    j = 0
    print("Welcome to the " + moduleName + " module.")
    while True:    
            if doneOrNot == "done":
                break
            else:
                usernameInput = input("Please enter " + moduleName + " username:")
                passwordInput = input("Please enter " + moduleName + " password:")
                i = 1
                for element in list:
                    if i < len(list) and list[i][int(usernameIndex)] == usernameInput and list[i][int(passwordIndex)] == passwordInput:
                        print("Logged in as " + usernameInput)
                        doneOrNot = "done"
                        break
                    if i == len(list):
                        if j == 4: 
                            print("Too many incorrect entries, try again later.")
                            quit()
                        else:
                            print("Incorrect username or password. Program will close after 5 incorrect entries. Please try again.")
                            j = j + 1
                    else:
                        i = i + 1 
    return usernameInput

                        
def login(fileName,moduleName):
    loginVerification(fileName)
    username = checkLoginInfo(findUsernameColumnIndex(fileName),findPasswordColumnIndex(fileName),loginVerification(fileName),moduleName)
    return username



