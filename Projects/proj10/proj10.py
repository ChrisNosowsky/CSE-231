import reversi
import string
from operator import itemgetter
LETTERS = string.ascii_lowercase

"""
Program runs the game Reversi. The program asks for a color, the board length, then starts asking to make moves on the board. 
The moves have to be strategic in order to win the game. Once the board is full, user wants to exit, or no moves are left, then the winner gets a cookie(not really).
"""

def indexify(position):
    """
    Takes in a position and stores as x, y. Binds to a list then converts to a tuple for return
    """
    if position[0] in LETTERS:
        x = LETTERS.find(position[0])
        y = int(position[1:]) - 1
        return (x,y)
def deindexify(row, col):
    """
    Takes in row and columns. The row will be used as an index for LETTERS. The column just gets +1.
    """
    let = LETTERS[row]
    num = str(col+1)
    return let+num

def initialize(board):
    """
    Initializes the board by giving it four pieces. Two black and two white that are placed in the center, diagonal from each other.
    """
    length = board.length
    even = int(length/2) - 1
    odd = int(length/2)
    board.place(even,even,reversi.Piece('white'))
    board.place(even,odd,reversi.Piece('black'))
    board.place(odd,even,reversi.Piece('black'))
    board.place(odd,odd,reversi.Piece('white'))
    
def count_pieces(board):
    """
    Counts total white and black pieces on board and returns total black and white pieces
    """
    row = board.length
    col = board.length
    black = 0
    white = 0
    for r in range(row):
        for c in range(col):
            b = board.get(r,c)
            if b != None:
                if b.is_white():
                    white += 1
                elif b.is_black():
                    black += 1
                else:
                    continue
    return (black,white)

def get_all_streaks(board, row, col, piece_arg):
    """
    Returns all the possible streaks at the given row,col. Returns it as a dictionary pointing to all the possible locations in each direction.
    """
    streaks = {'e': None, 'w': None, 'n': None, 's': None, \
               'ne': None, 'nw': None, 'se': None, 'sw': None}
    
    color = piece_arg.color()
    other_color = 'white' if color == 'black' else 'black'
    # north
    L = []
    c = col
    for r in range(row-1,-1,-1):
        if not board.is_free(r,c):
            piece = board.get(r,c)
            if piece.color() == other_color:
                L.append((r,c))
            else:
                break # terminated streak with color
        else:
            L = []  # terminated without finding color
            break
    else:
        L = [] # streak not terminated with color piece
    streaks['n'] = sorted(L)

#    # east
    L = []
    c = col
    r = row
    for c in range(col+1,board.length):
        if not board.is_free(r,c):
            piece = board.get(r,c)
            if piece.color() == other_color:
                L.append((r,c))
            else:
                break # terminated streak with color
        else:
            L = []  # terminated without finding color
            break
    else:
        L = [] # streak not terminated with color piece
    streaks['e'] = sorted(L)
 
#    # south
    L = []
    c = col
    r = row
    for r in range(row+1,board.length):
        if not board.is_free(r,c):
            piece = board.get(r,c)
            if piece.color() == other_color:
                L.append((r,c))
            else:
                break # terminated streak with color
        else:
            L = []  # terminated without finding color
            break
    else:
        L = [] # streak not terminated with color piece
    streaks['s'] = sorted(L)

#    # west
    L = []
    c = col
    r = row
    for c in range(col-1,-1,-1):
        if not board.is_free(r,c):
            piece = board.get(r,c)
            if piece.color() == other_color:
                L.append((r,c))
            else:
                break # terminated streak with color
        else:
            L = []  # terminated without finding color
            break
    else:
        L = [] # streak not terminated with color piece
    streaks['w'] = sorted(L)

#    # northeast
    L = []
    c = col
    r = row
    c = col+1
    for r in range(row-1,-1,-1):
        if c == board.length:
            L = []  # terminated without finding color
            break
        if not board.is_free(r,c):
            piece = board.get(r,c)
            if piece.color() == other_color:
                L.append((r,c))
            else:
                break # terminated streak with color
        else:
            L = []  # terminated without finding color
            break
        c += 1
    else:
        L = [] # streak not terminated with color piece
    streaks['ne'] = sorted(L)
        
#    # southeast
    L = []
    c = col
    r = row
    c = col+1
    for r in range(row+1,board.length):
        if c == board.length:
            L = []  # terminated without finding color
            break
        if not board.is_free(r,c):
            piece = board.get(r,c)
            if piece.color() == other_color:
                L.append((r,c))
            else:
                break # terminated streak with color
        else:
            L = []  # terminated without finding color
            break
        c += 1
    else:
        L = [] # streak not terminated with color piece
    streaks['se'] = sorted(L)
                
#    # southwest
    L = []
    c = col
    r = row
    c = col - 1
    for r in range(row+1,board.length):
        if c == -1:
            L = []  # terminated without finding color
            break
        if not board.is_free(r,c):
            piece = board.get(r,c)
            if piece.color() == other_color:
                L.append((r,c))
            else:
                break # terminated streak with color
        else:
            L = []  # terminated without finding color
            break
        c = c - 1
    else:
        L = [] # streak not terminated with color piece
    streaks['sw'] = sorted(L)
    
#    # northwest
    L = []
    c = col
    r = row
    c = col - 1
    for r in range(row-1,-1,-1):
        if c == -1:
            L = []  # terminated without finding color
            break
        if not board.is_free(r,c):
            piece = board.get(r,c)
            if piece.color() == other_color:
                L.append((r,c))
            else:
                break # terminated streak with color
        else:
            L = []  # terminated without finding color
            break
        c = c - 1
    else:
        L = [] # streak not terminated with color piece
    streaks['nw'] = sorted(L)
            
    return streaks

def get_all_capturing_cells(board, piece):
    """
    Gets all the nearby pieces that can be captured if the piece was placed down at the free board spot.
    """
    row = board.length
    col = board.length
    cell = {}
    for r in range(row):
        for c in range(col):
            if board.is_free(r,c):
                L = []
                streaks = get_all_streaks(board,r,c,piece)
                for v in streaks.values():
                    for n in v:
                        L.append(n)
                new = sorted(L)
                if L == []:
                    continue
                else:
                    cell.update({(r,c):new})
            else:
                continue
    return cell

def get_hint(board,piece):
    """
    Gives a hint at the best moves to make.
    """
    d = get_all_capturing_cells(board,piece)
    f =[]
    l = []
    g = []
    t = []
    for k in sorted(d, key=lambda k: len(d[k]), reverse=True):
        pos = k
        f.append((deindexify(pos[0],pos[1]),len(d[k])))
        g = sorted(f,key=itemgetter(0),reverse=True)
        l = sorted(g, key=itemgetter(1), reverse =True)
    for p in range(len(l)):
        t.append(l[p][0])
    return t
    
def place_and_flip(board, row, col, piece): 
    """
    Gets every streak possible with the given position and column and flips them. Prints error if the row,col is already occupied, if the position is outside the board, or if theres no moves possible.
    """
    i = 0
    l = board.length
    d = get_all_streaks(board,row,col,piece)
    if row > l or col > l:
        return "Error: Can't place {:s} at '{:s}',".format(piece.color()[0].upper(), deindexify(row,col)) + " invalid position. Type 'hint' to get suggestions."
    for key, val in d.items():
        if len(d[key]) > 0:
            if board.is_free(row,col) or i==1:
                i = 1
                board.place(row, col,piece)
                for val in d[key]:
                    if board.is_free(val[0],val[1]):
                        board.place(val[0],val[1],piece)
                    else:
                        board.place(val[0],val[1],piece)
            else:
                return "Error: Can't place {:s} at '{:s}',".format(piece.color()[0].upper(), deindexify(row,col)) + " already occupied. Type 'hint' to get suggestions."
    if i == 0:
        return "Error: Can't place {:s} at '{:s}',".format(piece.color()[0].upper(), deindexify(row,col)) + " it's not a capture. Type 'hint' to get suggestions."   
    return "suh" #ignore this
def is_game_finished(board):
    """
    Checks to see if the board is full or if there are no possible moves left to make. Returns True if game is done. False if not.
    """
    bp = reversi.Piece("black")
    wp = reversi.Piece("white")
    if board.is_full():
        return True
    elif len(get_all_capturing_cells(board,bp)) == 0 and len(get_all_capturing_cells(board,wp)) == 0:
        return True
    else:
        return False
            
def get_winner(board):
    """
    Counts the total white and black pieces on the board. Returns the color that wins, unless if they are equal, which in that case it will return draw
    """
    count = count_pieces(board)
    if count[0] > count[1]:
        return "black"
    elif count[0] < count[1]:
        return "white"
    else:
        return "draw"
    
def choose_color():
    """
    Let's the user choose a color he/she wants. If the color is not black or white, then an error message will come up and ask again.
    """
    test = True
    while test == True:
        color = input("Pick a color: ")
        if color.lower() == "black":
            my_color = "black"
            opponent_color = "white"
            test = False
        elif color.lower() == "white":
            my_color = "white"
            opponent_color = "black"
            test = False
        else:
            print("Wrong color, type only 'black' or 'white', try again.")
            
    print("You are '{:s}' and your opponent is '{:s}'.".format(my_color, opponent_color))
    return (my_color,opponent_color)

def game_play_human():
    """
    This is the main mechanism of the human vs. human game play.
    """
    
    banner = """
     _____                         _ 
    |  __ \                       (_)
    | |__) |_____   _____ _ __ ___ _ 
    |  _  // _ \ \ / / _ \ '__/ __| |
    | | \ \  __/\ V /  __/ |  \__ \ |
    |_|  \_\___| \_/ \___|_|  |___/_|
    
    Developed by The Students Inc.
    CSE231 Spring Semester 2018
    Michigan State University
    East Lansing, MI 48824, USA.
    """

    prompt = "[{:s}'s turn] :> "
    print(banner)
   
    # Choose the color here
    (my_color, opponent_color) = choose_color()
    
    # Take a board of size 8x8
    # Prompt for board size
    size = input("Input a board size: ")
    board = reversi.Board(int(size))
    initialize(board)
    
    # Decide on whose turn, use a variable called 'turn'.
    turn = my_color if my_color == 'white' else opponent_color
    
    # loop until the game is finished
    while not is_game_finished(board):
        try:
            # Count the pieces and assign into piece_count
            piece_count = count_pieces(board)
            
            print("Current board:")
            board.display(piece_count)    
            
            # Get a piece according to turn
            piece = reversi.Piece(turn)

            # Get the command from user using input
            command = input(prompt.format(turn)).lower()
            
            # Now decide on different commands
            if command == 'exit':
                break
            elif command == 'hint':
                print("\tHint: " + ", ".join(get_hint(board, piece)))
            elif command == 'pass':
                hint = get_hint(board, piece)
                if len(hint) == 0:
                    turn = my_color if turn == opponent_color \
                                        else opponent_color
                    print("\tHanded over to \'{:s}\'.".format(turn))
                else:
                    print("\tCan't hand over to opponent, you have moves," + \
                          " type \'hint\'.")
            else:
                    (row, col) = indexify(command)
                    t = place_and_flip(board, row, col, piece)
                    if "Error:" in t:
                        print(t)
                        continue
                    else:
                        print("\t{:s} played {:s}.".format(turn, command))
                        turn = my_color if turn == opponent_color \
                                            else opponent_color
        except Exception as err:
            print("Error:", err)
    
    # The loop is over.
    piece_count = count_pieces(board)
    print("Current board:")
    board.display(piece_count)    
    winner = get_winner(board)
    if winner != 'draw':
        diff = abs(piece_count[0] - piece_count[1])
        print("\'{:s}\' wins by {:d}! yay!!".format(winner, diff))
    else:
        print("This game ends in a draw.")
    # --- end of game play ---

def figure_1(board):
    """
    You can use this function to test your program
    """
    board.place(0,0,reversi.Piece('black'))
    board.place(0,3,reversi.Piece('black'))
    board.place(0,4,reversi.Piece('white'))
    board.place(0,5,reversi.Piece('white'))
    board.place(0,6,reversi.Piece('white'))
    board.place(1,1,reversi.Piece('white'))
    board.place(1,3,reversi.Piece('white'))
    board.place(1,5,reversi.Piece('white'))
    board.place(1,6,reversi.Piece('white'))
    board.place(1,7,reversi.Piece('white'))
    board.place(2,2,reversi.Piece('white'))
    board.place(2,3,reversi.Piece('black'))
    board.place(2,4,reversi.Piece('white'))
    board.place(2,5,reversi.Piece('white'))
    board.place(2,7,reversi.Piece('white'))
    board.place(3,0,reversi.Piece('black'))
    board.place(3,1,reversi.Piece('white'))
    board.place(3,2,reversi.Piece('white'))
    board.place(3,4,reversi.Piece('white'))
    board.place(3,5,reversi.Piece('white'))
    board.place(3,6,reversi.Piece('black'))
    board.place(3,7,reversi.Piece('black'))
    board.place(4,0,reversi.Piece('white'))
    board.place(4,2,reversi.Piece('white'))
    board.place(4,4,reversi.Piece('white'))
    board.place(5,0,reversi.Piece('black'))
    board.place(5,2,reversi.Piece('black'))
    board.place(5,3,reversi.Piece('white'))
    board.place(5,5,reversi.Piece('black'))
    board.place(6,0,reversi.Piece('black'))
    board.place(6,1,reversi.Piece('black'))
    board.place(6,3,reversi.Piece('white'))
    board.place(6,6,reversi.Piece('white'))
    board.place(7,1,reversi.Piece('black'))
    board.place(7,2,reversi.Piece('white'))
    board.place(7,3,reversi.Piece('black'))
    board.place(7,7,reversi.Piece('black'))
    
if __name__ == "__main__":
    game_play_human()
