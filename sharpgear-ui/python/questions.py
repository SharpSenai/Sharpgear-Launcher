# Libraries
from InquirerPy import inquirer as inputPy
import re 

# Questions

class promptLoginRegister():
    
    def promptLoginRegister(self):
        self.method  = inputPy.select(
            message="Select your login method:",
            choices=["Login", "SignUp"],
        ).execute()
        
        match self.method:
            case "Login":
                
                self.user     = None
                self.password = None
                
                def promptUsername():
                    self.user = inputPy.text(message="Type your username:").execute()
                    if self.user == "":
                        promptUsername()
                    
                    return self.user
                
                def promptPassword():
                    self.password = inputPy.text(message="Type your password:").execute()
                    if self.password == "":
                        promptPassword()
                
                promptUsername()
                promptPassword()
                
                print(self.user, self.password)
            
            
            
pLR = promptLoginRegister()
pLR.promptLoginRegister()