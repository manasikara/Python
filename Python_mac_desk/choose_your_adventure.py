# learning source --> https://www.youtube.com/watch?v=DLn3jOsNRVE&list=PLE3yaxY1qUqOg2_EV35loEGXnC8nuSbrn&index=12

name = input("Type your name: ")

print = input("Welcome " + name + " to this Pixel Adventure!. Use the capitalised words as an answer")

answer = input("You're in your room, in front of your PC. The PC is turned off. Do you want to START it or LEAVE the room in order to do some useless activities? ").lower()

if answer == "start":
    answer = input("A beautifull beep sound had been played and you see the 'Welcome to the Pixel World' writing on the screen. Do you want to LOG-IN, or SHUTDOWN?")
    
    if answer == "log-in":
        print("Start exploring! + name")
    elif answer == "shutdown":
      print("Bye + name")
    else:
        print("Not a valid option, looser!")    
            

elif answer == "leave":
    print("You really mus'nt like the Pixel World. Bye.")

else:
    print("Not a valid option, looser!")    
    
    #TBC...