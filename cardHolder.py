class cardHolder():
    def __init__( self, cardNum, code, firstname, lastname, balance):
      self.cardNum = cardNum
      self.code = code
      self.firstname = firstname
      self.lastname = lastname
      self.balance = balance
        
  ### getter methods
def get_cardNum(self):
      return self.cardNum
def get_code(self):
      return self.code  
def get_firstname(self):
      return self.firstname          
def get_lastname(self):
      return self.lastname
def get_balance(self):
      return self.balance  
      
    ###setter methods  
def set_cardNum(self, newVal):
      self.cardNum = newVal
def set_code(self, newVal):
      self.code = newVal                
def set_firstname(self, newVal):
      self.firstname =newVal
def set_lastname(self, newVal):
      self.lastname = newVal
def set_balance(self, newVal):
      self.balance = newVal   
       

def print_out(self):
   print("Card #:", self.cardNum)
   print("Code #:", self.code)
   print("First Name #:", self.firstname)
   print("Last Name #:", self.lastname)           
   print("Balance #:", self.balance)