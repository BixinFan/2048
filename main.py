#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import game_functions as gf

def main():
    board = gf.initialize_game()
    game_over = False

    while not game_over:
        print_board(board)
        move = input("Enter move (w/a/s/d): ")

        try:
            if move == 'w':
                board = gf.move_up(board)
            elif move == 's':
                board = gf.move_down(board)
            elif move == 'a':
                board = gf.move_left(board)
            elif move == 'd':
                board = gf.move_right(board)
            else:
                raise ValueError("Invalid Move. Please enter w, a, s, or d.")
            
            gf.add_new_tile(board)
            status = gf.get_current_state(board)
            if status == 'WIN':
                print_board(board)
                print("Congratulations, you've won!")
                break
            elif status == 'LOSE':
                print_board(board)
                print("Game Over. Try again!")
                break
        except ValueError as ve:
            print(ve)

def print_board(board):
    """ Print the current game board. """
    for row in board:
        print("\t".join([str(num) if num != 0 else '.' for num in row]))
    print()

if __name__ == "__main__":
    main()

