#Aleks Calderon
#6.8.2019
#login feature for chat application


def loginFeature():

    account = str(input("Would you like to create an account?"))
    if (account == "yes" or account == "Yes"):
#creates new user
        username = str(input("Please create your username: "))
    #opens and reads username list to see which user is on there
        user = open("accountList.txt","r") 

        for x in user:

            x = x.split(", ")
            print(x)
    #checks if username is on list already
            if username == x[0]:
                usernameRedo = str(input("This user already exits! Please create a new username: "))
            if x not in user:
                user = open("accountList.txt", "a+")
                password = str(input("Please create your password: "))
                user.write(username + ", " + password + "\n")
                

                
    else:
        userLogin = str(input ("Enter your username: "))
        user = open("accountList.txt", "r" )
        for x in user:
            y = x.split(", ")
            
            if userLogin == y[0]:
                passwordCheck = str(input("Enter your password: "))
                if passwordCheck == y[1]:
                    successfulLogin = print("Welcome, "+ userLogin)
        #if username is usernameList:
            #passwordLogin = str(input ("Enter your password: "))
           # if passwordLogin != passwordList:
                #accessLogin = print("Welcome, " + username)
                else:
                    print("This user does not exist. Please try again or create a new account.")
                #account = str(input("Would you like to create an account?"))
                                    
loginFeature()
