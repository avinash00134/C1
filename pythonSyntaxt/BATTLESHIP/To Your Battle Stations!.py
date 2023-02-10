from random import randint

board = []

for x in range(0, 5):
  board.append(["O"] * 5)

def print_board(board):
  for row in board:
    print " ".join(row)

print_board(board)

def random_row(board):
  return randint(0, len(board) - 1)

def random_col(board):
  return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)
print ship_row
print ship_col

# Everything from here on should be in your for loop
# don't forget to properly indent!
for turn in range(4):
  print "Turn", turn + 1
  guess_row = int(raw_input("Guess Row: "))
  guess_col = int(raw_input("Guess Col: "))

  if guess_row == ship_row and guess_col == ship_col:
    print "Congratulations! You sank my battleship!"
    break
  else:
    if guess_row not in range(5) or \
      guess_col not in range(5):
      print "Oops, that's not even in the ocean."
    elif board[guess_row][guess_col] == "X":
      print( "You guessed that one already." )
    else:
      print "You missed my battleship!"
      board[guess_row][guess_col] = "X"
    if (turn == 3):
      print "Game Over"
    print_board(board)
    
# Extra Credit

# command line clender

'''
Codeacedemy
Command Line Calendar'''

from time import sleep, strftime
FIRST_NAME = "Avinash sharma"
calender = {}
def welcome():
    print("Welcome " + FIRST_NAME + "\nOpening the calender.")
    sleep(1)
    print(strftime("%A %B %dth, %Y"))
    print(strftime("%I:%M:%S%p"))
    sleep(1)
    print("What would you like to do?")
def start_calendar():
    welcome()
    start = True
    while(start):
        user_choice = input(
            "A to Add, U to Update, V to View, D to Delete, X to Exit: ")
        user_choice = user_choice.upper()
        if user_choice == 'V':
            if bool(calender) == False:
                print("Calender is empty.")
            else:
                print(calender)
        elif user_choice == 'U':
            date = input("What date?: ")
            update = input("Enter the update: ")
            calender[date] = update
            print("Update successful.")
            print(calender)
        elif user_choice == 'A':
            event = input("Enter event: ")
            date = input("Enter date (MM/DD/YYYY): ")
            print(date[6:10])
            if len(date) > 10 or int(date[6:10]) - int(strftime("%Y")) > 0:
                print("Invalid date was entered.")
                
                try_again = input("Try Again? Y for Yes, N for No: ")
                try_again = try_again.upper()
                if try_again == 'Y':
                    continue
                elif try_again == 'N':
                    print("Exiting program.")
                    start = False
            else:
                calender[date] = event
                print("Event was sucessfully added.")
                print(calender)
        elif user_choice == 'D':
            if bool(calender) == False:
                print("Calender is empty.")
            else:
                event = input("What event?: ")
                for date in calender:
                    if event == calender[date]:
                        del calender[date]
                        print("Event was successfully deleted.")
                    else:
                        print("Incorrect event was specified.")
        elif user_choice == 'X':
            start = False
        else:
            print("Invalid command wasentered. Program exiting.")
            start = False
start_calendar()


# 