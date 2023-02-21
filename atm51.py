from cardHolder import cardHolder

def print_menu():
###print options to the user 
  print("please choose from one of the following options...")
print("1.Deposit")
print("2.Withdraw")
print("3. Show Balance")
print("4.Exit")

def deposit(cardHolder):
  try: 
    deposit = float(input("how much RS. would you like to seposit"))
    cardHolder.set_balance(cardHolder.get_balance()+deposit)
    print("Your new balance is:", str(cardHolder.get_balance))
  except:
    print("Invalid input")

def withdraw(cardHolder):
    try:

      withdraw = int(input("how much money you want to withdraw"))
      if ( cardHolder.get_balance() < withdraw):
        print("insufficient balance:(")
      else:
        cardHolder.set_balance(cardHolder.get_balance()-withdraw)
      print("You are good to go!Thankyou :)")
    except:
      print("invalid input")

def check_balance(cardHolder):
  print("Your current balance is:",cardHolder.get_balance())
  if _name_ == "__main__":
    current_user = cardHolder("","","","")
    list_of_cardHolders =[]
    list_of_cardHolders.append(cardHolder("5728582",1234, "Dips", "agg", 160))
    list_of_cardHolders.append(cardHolder("6439692",5678, "Dip", "ag", 1600))
    list_of_cardHolders.append(cardHolder("5378253",9123, "Di", "ag", 16000))
    list_of_cardHolders.append(cardHolder("5285827",4567, "D", "aggg", 16000))
    list_of_cardHolders.append(cardHolder("4626472",8912, "D.", "aggg", 1600000))
    debitCardNum =""
    while True:
      try:
        debitCardNum =input("please insert your debit card:")
        debitMatch =[holder for holder in list_of_cardHolders if holder.cardNumm== debitCardNum]
        if (len(debiMatch)>0):
          current_user =debitMatch[0]
          break
        else:
          print("cardnuber not recognised")
      except:
        print("card number not recognised. please try again")
        while True:
          try:
            userCode = int(input("please enter your pin: ").strip())
            if(current_user.get_code() == userCode):
              break
            else:
              print("Invalid pin. please try again") 
          except:
            print("invalid pin, please try again")
            print("Welcome",current_user.get_firstname(), "  :)")
            option =0
            while True:
              print_menu()
              try:
                option= int(input())
              except:
                print("invalid input. please try again.")
                if(option == 1):
                  deposit(current_user)
                elif(option == 2):
                  withdraw(current_user)
                elif(option == 3):
                  check_balance(current_user)
                elif(option == 4):
                  break
                else:
                  (option == 0)
                  print("Thankyou, have a nice day: )")
                    
                