#Mastermind Computer Game

def menu():

    print('Welcome to the Mastermind Computer Game!')
    print()
    print('================MAIN MENU==================')
    print()
    print('1. PLAY!')
    print('2. HOW TO PLAY?')
    print('3. EXIT')
    print('***************')
    print()

    choice=input('Enter a number(1/2/3) to continue: ')
    print()
    
    if choice=='1':
        play=='Y'
    elif choice=='2':
        instruction()
    elif choice=='3':
        raise SystemExit

def play():

        if play=='Y':
            game()
            
def instruction():
        
    print('----------------HOW TO PLAY?---------------')
    print('Colour selections available are R(red),O(orange),Y(yellow),G(green),B(blue),P(purple).')
    print('Note that repetitions are allowed.')
    print('Have fun and good luck!')
    start=input('Play now?(Y/N)').upper()
    print(start)

    if start!='Y':
        menu()
    
def game():
    
    import random
    colours=['R','O','Y','G','B','P']
    random1=random.choice(colours)
    random2=random.choice(colours)
    random3=random.choice(colours)
    random4=random.choice(colours)

    randomList=[random1,random2,random3,random4]
    print(randomList)
            
    guesses=0

    while True:

        colour=0
        wrong=0
    
        while True:
            c1=input('Guess the first colour:').upper()
            if c1 not in colours:
                print('Invalid input. Please try again.')
            else:
                break
        
        while True:
            c2=input('Guess the second colour:').upper()
            if c2 not in colours:
                print('Invalid input. Please try again.')
            else:
                break

        while True:
            c3=input('Guess the third colour:').upper()
            if c3 not in colours:
                print('Invalid input. Please try again.')
            else:
                break

        while True:
            c4=input('Guess the fourth colour:').upper()
            if c4 not in colours:
                print('Invalid input. Please try again.')
            else:
                break

        colourList=[c1,c2,c3,c4]

        colourListIndex=[0,1,2,3]
        randomListIndex=[0,1,2,3]

        for i in range(4):
            if colourList[i] == randomList[i]:
                colour+=1
                randomListIndex.remove(i)
                colourListIndex.remove(i)

        newColourList=[]
        newRandomList=[]

        for i in randomListIndex:
            newRandomList.append(randomList[i])

        for i in colourListIndex:
            newColourList.append(colourList[i])

        for i in range(len(randomListIndex)):
            if newColourList[i] in newRandomList:
                element=newColourList[i]
                wrong+=1
                newRandomList.remove(element)
                
        if colour==4:
            guesses+=1
            print('Congratulations!You got it right!')
            print()
            break
        else:
            print('Please try again')
            print()

        print()
        print('Correct colour in the correct place:',colour)
        print('Correct colour but in the wrong place:',wrong)
        print()

        guesses+=1
        
    if guesses==1:
        print('It only took you',guesses,'guess!')
    else:
        print('It only took you',guesses,'guesses!')

    print()

def replay():
    
    play=input('Would you like to play again?(Y/N)').upper()
    while play!='Y' and play!='N':
        print('Please respond with a Y or N')

    while play=='Y':
        menu()
        game()
        replay()
        break

    
    while play=='N':
        print('Goodbye and hope to see you again')
        print('Thank you for playing!!!')
        break

menu()

play='Y'
while play=='Y':

    game()
    replay()
    break
