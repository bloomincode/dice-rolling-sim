import random

def print_dice(roll_val):
    dice_outline_t = "   -------  "
    dice_outline_b = "  -------  "
    top_line = " |       | "
    mid_line = " |       | "
    bot_line = " |       | "

    if roll_val == 1:
        mid_line = " |   0   | "
    elif roll_val == 2:
        top_line = " | 0     | "
        bot_line = " |     0 | "
    elif roll_val == 3:
        mid_line = " |0  0  0| "
    elif roll_val == 4:
        top_line = " |0     0|"
        bot_line = " |0     0|"
    elif roll_val == 5:
        top_line = " |0     0| "
        mid_line = " |   0   | "
        bot_line = " |0     0| "
    else:
        top_line = " |0  0  0| "
        bot_line = " |0  0  0| "
    
    print(dice_outline_t, "\n",top_line, "\n", mid_line, "\n", bot_line, "\n", dice_outline_b)

def main():
    print("Enter y to roll the dice")
    user_response = input()
    
    while(user_response == 'y'):
        if user_response == 'y':
            roll_val = random.randint(1,6)
        print_dice(roll_val)
       
        print("Enter y to roll the dice again")
        user_response = input()
        
if __name__ == '__main__':
    main()