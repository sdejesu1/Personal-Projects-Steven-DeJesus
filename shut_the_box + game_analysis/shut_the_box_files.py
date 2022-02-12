#Author: Steven De Jesus


#define constants
MIN = 1
MAX = 5
SIMULATIONS = 100
# import random
import random

# main fxn
def main():
    # display title
    print("Let's play Shut the Box!")
    turn = 0
    block_1 = False
    block_2 = False
    block_3 = False
    block_4 = False
    block_5 = False
    num_dice_not_used = 0
    while num_dice_not_used <= 2:
        # display current turn
        turn = turn + 1
        print(f'Turn: {turn}')
    
        # call roll die fxn twice to get values for the round
        die_1 = roll_die()
        die_2 = roll_die()
        num_dice_not_used = 0
        # display the values rolled
        print(f'You rolled a {die_1} and a {die_2}')

        # re establish bool variable after die rolled
        # die_1 
        if die_1 == 1:
            if block_1:
                num_dice_not_used += 1
            if block_1 == False:
                block_1 = True
                print('You knocked down block 1')

                
        elif die_1 == 2:
            if block_2:
                num_dice_not_used += 1
            if block_2 == False:
                block_2 = True
                print('You knocked down block 2')
     
        elif die_1 == 3:
            if block_3:
                num_dice_not_used += 1
            if block_3 == False:
                block_3 = True
                print('You knocked down block 3')
           
                
        elif die_1 == 4:
            if block_4:
                num_dice_not_used += 1
            if block_4 == False:
                block_4 = True
                print('You knocked down block 4')

                
        elif die_1 == 5:
            if block_5:
                num_dice_not_used += 1
            if block_5 == False:
                block_5 = True
                print('You knocked down block 5')
                
        # die_2
        if die_2 == 1:
            if block_1:
                num_dice_not_used += 1
            if block_1 == False:
                block_1 = True
                print('You knocked down block 1')

                
        elif die_2 == 2:
            if block_2:
                num_dice_not_used += 1
            if block_2 == False:
                block_2 = True
                print('You knocked down block 2')
     
        elif die_2 == 3:
            if block_3:
                num_dice_not_used += 1
            if block_3 == False:
                block_3 = True
                print('You knocked down block 3')
           
                
        elif die_2 == 4:
            if block_4:
                num_dice_not_used += 1
            if block_4 == False:
                block_4 = True
                print('You knocked down block 4')

                
        elif die_2 == 5:
            if block_5:
                num_dice_not_used += 1
            if block_5 == False:
                block_5 = True
                print('You knocked down block 5')


        if num_dice_not_used == 2:
            print(f'You lost in {turn} turns, better luck next time.')
            verdict = "Lost"
            write_to_file(verdict)
            num_dice_not_used += 1

        #set condition for if has won is true
        elif has_won(block_1, block_2, block_3, block_4, block_5):
            print(f'Congrats! You won in {turn} turns!')
            verdict = "Won"
            write_to_file(verdict)
            num_dice_not_used += 3
     
# has won fxn
def has_won(block_1, block_2, block_3, block_4, block_5):
    return block_1 and block_2 and block_3 and block_4 and block_5

# roll die fxn
def roll_die():
    return random.randint (MIN, MAX)

# write to file fxn
# take one parameter, string that is either won or lost
def write_to_file(verdict):
        # append data to analysis_data.txt
        # if string is won
        if verdict == "Won":
            out_file = open("analysis_data.txt", "a")
            out_file.write(str(verdict) + "\n")
            out_file.close
      
        

        # if string is lost
        elif verdict == "Lost":
            out_file = open("analysis_data.txt", "a")
            out_file.write(str(verdict) + "\n")
            out_file.close
   
    

# run fxn but with simulations = 100
SIMULATIONS = 100
for trial in range(SIMULATIONS + 1):
    main()
