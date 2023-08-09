#https://youtu.be/DLn3jOsNRVE

print('Welcome to my computer quiz')

playing = input('Do you want to play? ')
if playing == 'yes':
    print("OK! Let's play")
if playing == 'no':
    print('To co mi zawracasz dupę?')
    quit()

score = 0

answer = input('What does CPU stand for? ').lower()
if answer == 'central processing unit':
    print('Correct!')
    score += 1
else:
    print('Wrong answer')

answer = input('What does GPU stand for? ').lower()
if answer == 'graphic processing unit':
    print('Correct!')
    score += 1
else:
    print('Wrong answer')
    
answer = input('What does RAM stand for? ').lower()
if answer == 'random access memory':
    print('Correct!')
    score += 1
else:
    print('Wrong answer')    
    
answer = input('CRT, TFT, DLP or LED ? ').lower()
if answer == 'monitor':
    print('Correct!')
    score += 1
else:
    print('Wrong answer')

answer = input('What is the newest USB version? ').lower()
if answer == '3.2':
    print('Correct!')
    score += 1
else:
    print('Wrong answer')        
    
print('You got ' + str(score) + ' questions correct!')
print('You got ' + str((score / 5) * 100) + '%.')
