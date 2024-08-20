class ATM:
     def screen(self,pin = "Ammar"):
          pin_ver =self.__verifier(pin)
          display =self.__sender(pin_ver)
          return display

     def __verifier(self,pin_ver):
          if pin_ver  :
               return True
          else:
           return False



     def __sender(self,pin_ver):  
          if pin_ver == "Ammar":
               return "You are fuyll"
          else:
           return "go to home"    

user =ATM()
print(user.screen("wgwer"))         