print("Welcome To Treasure Island! Lets find the treasure!")

pos = input("Would You Go Left or Right?\n")

if pos == 'right' or pos == 'Right':
    print("Game Over!")
else:
    pos = input("Would You Like to swim or wait?\n")
    if pos == 'Swim' or pos == 'swim':
        print("Game Over!")
    else:
        pos = input('Which Door You Want to choose?\nYellow, Blue or Red')
        if pos == 'yellow' or pos == 'Yellow':
            print('You Win!')
        else:
            print("Game Over!")

