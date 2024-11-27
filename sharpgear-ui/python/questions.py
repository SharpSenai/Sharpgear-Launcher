# Libraries
from InquirerPy import inquirer as inputPy
from validation import *
from database import DataBase


# Questions

class promptQuestions():
    def __init__(self):
        self.db = DataBase()
    
    def promptLoginRegister(self):
        self.method  = inputPy.select(
            message="Select your login method:",
            choices=["Login", "SignUp"],
        ).execute()
        
        match self.method:
            case "Login":
                
                def promptUsername():
                    self.user = inputPy.text(message="Type your username or email:").execute()
                    if self.user == "":
                        promptUsername()
                    
                    return self.user
                
                def promptPassword():
                    self.password = inputPy.text(message="Type your password:").execute()
                    if self.password == "":
                        promptPassword()
                
                promptUsername()
                promptPassword()
                
                success = self.db.queryInformation("checkLogin",
                                                   (self.user, self.user, self.password))
                
                if success:
                    
                    print(f"Logged successfully as: {self.user}")
                    
                    success = self.db.queryInformation("returnInfo", ("username", self.user))
                    if success:
                        print(success)
                    
                else:
                    print("Wrong credentials, try again.")
                    self.user = None 
                    self.password = None
                    self.promptLoginRegister()
                    
                
            case "SignUp":
                def promptUsername():
                    self.user = inputPy.text(message="Type your account username:").execute()
                    isValid = validate_username(self.user)
                    
                    if not isValid:
                        promptUsername()
                        
                def promptPassword():
                    self.password = inputPy.text(message="Type a password:").execute()
                    isValid = validate_password(self.password)
                    
                    if not isValid:
                        promptPassword()
                
                def promptEmail():
                    self.email = inputPy.text(message="Type your email:").execute()
                    isValid = validate_email(self.email)
                    
                    if not isValid:
                        promptEmail()
                        
                def promptPersona():
                    self.persona = inputPy.text(message="Type your full name:").execute()
                    isValid = validate_persona
                    
                    if not isValid:
                        promptPersona()
                        
                def promptBirthday():
                    self.birthday = inputPy.text(message="Type your birthday date:").execute()
                    isValid = validate_birthday(self.birthday)
                    
                    if not isValid:
                        promptBirthday()
                 
                promptPersona()    
                promptUsername()
                promptPassword()
                promptEmail()
                promptBirthday()
                
                success = self.db.queryInformation("registerAccount", (self.persona, self.user, self.email, self.password, self.birthday,))
                
                if success:
                    print("Created your account successfully!")
                else:
                    print("Couldn't create your account, try again.")
            
    def promptMenu(self):
        self.method = inputPy.select(
            message="Welcome to the main menu, where do you want to go?",
            choices=["Library", "Shop", "Profile"]
        ).execute()

        match self.method:
            case "Library":
                self.openLibrary()

            case "Shop":
                self.openShop()

            case "Profile":
                self.openProfile()

    def openLibrary(self):
        print("Opening Library...")

    def openShop(self):
        print("Opening Shop...")

    def openProfile(self):
        print("Opening Profile...")

                
                
            
        
            
pLR = promptQuestions()
pLR.promptLoginRegister()