# learning source --> https://www.youtube.com/watch?v=DLn3jOsNRVE&list=PLE3yaxY1qUqOg2_EV35loEGXnC8nuSbrn&index=12

name = input("Type your name:")
print = input("Welcome", name, "to this pixel adventure!. Use the capitalised words as an answer, please.")
answer = input("You're in your room, in front of your PC. The PC is turned off. Do you want to START it or LEAVE the room in order to do some useless activities?")

if answer == "start":
    answer = input("A beautifull beep sound had been played and you see the 'welcome' screen on the monitor. Do you want to LOG-IN, or SHUTDOWN?")
    if answer == "log-in":
        print()
    elif answer == "shutdown":
      print()
    else:
        print("Not a valid option, looser!")    
            

elif answer == "leave":
    print()

else:
    print("Not a valid option, looser!")    
    
    #TBC...