import re
email_re = r'\b[a-z0-9._%+-]+@[a-z0-9.-]+\.[A-Z|a-z]{2,}\b'
password_re="^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"

#Login part

def login(email,password):
    success=False
    file = open("user_details.txt","r")
    for i in file:
        a,b =i.split(",")
        b = b.strip()
        if(a==email and b==password):
            success=True
            break
    file.close()
    if (success):
        print("Login Successful !!!")
    else:
        print("Details not fount, Please Register")

#Register part       

def register(email,password):

    file = open("user_details.txt","a")
    file.write(email+", "+password+"\n")
    file.close()

#Accessing Login & Register part

def access(option):
    
    if (option== "Login"):
        email = input("Enter your Mail id: ")
        password = input("Enter your Password: ")
        login(email,password)
    else:
        print("Enter Details to Register")
        email = input("Enter your Mail id: ")
        password = input("Enter your Password: ")
        if(re.fullmatch(email_re, email)):
            if(re.fullmatch(password_re, password)):
                register(email,password)
            else:
                print("Password is not valid")
                access(option)
        else:
            print("Email is not valid")
            access(option)

#starting part - main sourse   
      
def start():
    global option
    option = input("Login or Register: ")
    if (option != "Login" and option != "Register"):
        print("retry!!!")
        start()
   
start()
access(option)