command = ""
started=False 
while True:
 command =input("< ").lower()
 if command == "start" :
     if started:
        print ("Car has already started ")
     else :
         started=True
         print ("Car started")
 elif command =="stop":
     if not started :
        print ("already stopped ,bro what the fuck ! !")
     else :
         started =False
         print ("stopped")  
 elif command =="help":
     print("""
        start - to start the car 
      stop- to stop the car
     quit - to leave the game 
     """)  
 elif command == "quit":
     break
 else :
     print("I don't understand the command")          