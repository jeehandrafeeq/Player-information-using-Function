print("Cricket Player Information")
print("1-Virat Kohli 2-Rohit Sharma 3-KL Rohul 4-Ms Dhone 5-sachin Tendulkar")
def ViratKholi():
    print("Player Name:Virat Kholi\nAge:38\nRole:Right Hand Batsman")
def RohitSharma():
    print("Player Name:Virat Kholi\nAge:38\nRole:Right Hand Batsman")
def KLRohul():
    print("Player Name:Virat Kholi\nAge:38\nRole:Right Hand Batsman")
def MsDhone():
    print("Player Name:Virat Kholi\nAge:38\nRole:Right Hand Batsman")    
def sachinTendulkar():
    print("Player Name:Virat Kholi\nAge:38\nRole:Right Hand Batsman")
while True:

    user=input("enter which player that you want some information:").upper()

    if user=="1":
      ViratKholi()
    elif user=="2":
      RohitSharma()   
    elif user=="3":
      KLRohul()
    elif user=="4":
      MsDhone()
    elif user=="5":
      sachinTendulkar() 

    elif user=="all":
      ViratKholi()
      RohitSharma()
      KLRohul()
      MsDhone()
      sachinTendulkar()

    else:
      print("This player is not added")