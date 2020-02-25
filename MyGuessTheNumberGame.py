#Guess the number game with unlimited attempts
import random, sys
randomNumber=random.randint(1,20)
print('I am thinking of a number between 1 and 20 and you have unlimited attempts')

numberGuessed=0
while True:
    print('Take a guess or enter "99" to quit')
    myGuess=int(input())
    if myGuess==99:
        sys.exit()
    elif myGuess<randomNumber:
        print('Too low')
        numberGuessed=numberGuessed+1
    elif myGuess>randomNumber:
        print('Too high')
        numberGuessed=numberGuessed+1
    else:
        break #means input was correct

if myGuess==randomNumber:
    print('Nice! You did it in ' +str(numberGuessed)+' guesses!')

else:
    print('Buuu. The number i was thinking about was '+str(randomNumber)+' . Better luck next time!')

