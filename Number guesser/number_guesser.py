# https://pyglet.readthedocs.io/en/latest/modules/media.html
# https://youtu.be/DLn3jOsNRVE

import random
import pyglet
import time

type_a_number=pyglet.media.load('\\Users\\slawe\\iCloudDrive\\gitRepos\\Python\\Number guesser\\sounds\\type_a_number.wav')

larger=pyglet.media.load('\\Users\\slawe\\iCloudDrive\\gitRepos\\Python\\Number guesser\\sounds\\larger.wav')

number_next_time=pyglet.media.load('\\Users\\slawe\\iCloudDrive\\gitRepos\\Python\\Number guesser\\sounds\\number_next_time.wav')

bingo=pyglet.media.load('\\Users\\slawe\\iCloudDrive\\gitRepos\\Python\\Number guesser\\sounds\\bingo.wav')

above=pyglet.media.load('\\Users\\slawe\\iCloudDrive\\gitRepos\\Python\\Number guesser\\sounds\\above.wav')

below=pyglet.media.load('\\Users\\slawe\\iCloudDrive\\gitRepos\\Python\\Number guesser\\sounds\\below.wav')

got_it=pyglet.media.load('\\Users\\slawe\\iCloudDrive\\gitRepos\\Python\\Number guesser\\sounds\\got_it.wav')

thanks=pyglet.media.load('\\Users\\slawe\\iCloudDrive\\gitRepos\\Python\\Number guesser\\sounds\\thanks.wav')

type_a_number.play()
top_of_range = input("Type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        larger.play()
        print('Type a number larger than 0 next time, please.')
        quit()

else:
    number_next_time.play()
    print('Please type a number next time.')
    quit()

random_number = random.randint(0, top_of_range)
guesses = 0

while True:
    guesses += 1
    user_guess = input('Make a guess: ')
    if  user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        number_next_time.play()
        print('Please type a number next time.')
        continue  
    
    if user_guess == random_number:
        bingo.play()
        print("Bingo!")
        break
    
    elif user_guess > random_number:
        above.play()
        print('You were above the number!')
        
    else:
        below.play()
        print('You were below the number!')

got_it.play()        
print('You got it in', guesses, 'guesses')

time.sleep(2)

thanks.play()
print('Thanks for the game')

time.sleep(4)

# to be continued....
