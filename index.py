def display_rules():
    print("\n--- 21 NUMBER GAME RULES ---")
    print("1. Players take turns counting up from 1 to 21.")
    print("2. On your turn, you can call out 1, 2, or 3 consecutive numbers.")
    print("3. The player who is forced to call '21' loses the game.\n")

def get_player_move(current_number):
    while True:
        try:
            print(f"Current count is: {current_number}")
            choice = int(input("How many numbers do you want to add? (1, 2, or 3): "))
            if choice in [1, 2, 3]:
                return choice
            print("Invalid input. You can only choose 1, 2, or 3 numbers.")
        except ValueError:
            print("Please enter a valid integer (1, 2, or 3).")

def play_game():
    display_rules()
    
    while True:
        order = input("Do you want to go first? (y/n): ").strip().lower()
        if order in ['y', 'n']:
            break
        print("Invalid choice. Please enter 'y' or 'n'.")
        
    current_number = 0
    is_player_turn = True if order == 'y' else False
    
    while current_number < 21:
        if is_player_turn:
            print("\n--- Your Turn ---")
            choices = get_player_move(current_number)
            
            print("You called: ", end="")
            for _ in range(choices):
                current_number += 1
                print(current_number, end=" ")
            print()
            
            if current_number >= 21:
                print("\nYou had to say 21! **You LOSE.** Computer wins!")
                return
                
            is_player_turn = False
        else:
            print("\n--- Computer's Turn ---")
            # Mathematical Strategy: force the cumulative count to a multiple of 4
            remainder = current_number % 4
            if remainder == 0:
                # If the user played perfectly, computer falls back to picking 1 number
                comp_choices = 1
            else:
                comp_choices = 4 - remainder
                
            print("Computer called: ", end="")
            for _ in range(comp_choices):
                current_number += 1
                print(current_number, end=" ")
            print()
            
            if current_number >= 21:
                print("\nComputer had to say 21! **You WIN!**")
                return
                
            is_player_turn = True

if __name__ == "__main__":
    play_game()
