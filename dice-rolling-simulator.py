import random

def print_dice(roll_val):
    dice_outline = "  -------  "
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
        top_line = " |0     0| "
        bot_line = " |0     0| "
    elif roll_val == 5:
        top_line = " |0     0| "
        mid_line = " |   0   | "
        bot_line = " |0     0| "
    else:
        top_line = " |0  0  0| "
        bot_line = " |0  0  0| "
    
    print(dice_outline)
    print(top_line)
    print(mid_line)
    print(bot_line)
    print(dice_outline)

def main():
    print("Enter y to roll the dice")
    user_response = input()
    if user_response == 'y':
        roll_val = random.randint(1,6)
    print_dice(roll_val)

if __name__ == '__main__':
    main()