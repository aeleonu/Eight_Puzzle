#
# board.py (Final Project)
#
# A Board class for the Eight Puzzle
#
# name: 
# email:
#
# If you worked with a partner, put his or her contact info below:
# partner's name:
# partner's email:
#

class Board:
    """ A class for objects that represent an Eight Puzzle board.
    """
    def __init__(self, digitstr):
        """ a constructor for a Board object whose configuration
            is specified by the input digitstr
            input: digitstr is a permutation of the digits 0-9
        """
        # check that digitstr is 9-character string
        # containing all digits from 0-9
        assert(len(digitstr) == 9)
        for x in range(9):
            assert(str(x) in digitstr)

        self.tiles = [[0] * 3 for x in range(3)] 
        self.blank_r = -1
        self.blank_c = -1

        b = 0
        
        for row in range(len(self.tiles)):
            for col in range(len(self.tiles[0])):
                self.tiles[row][col] = int(digitstr[b])
                b += 1
                if self.tiles[row][col] == 0:
                    self.blank_r = row
                    self.blank_c = col

        self.digitstr = digitstr        
        
    ### Add your other method definitions below. ###
    def __repr__(self):
        """ returns a string representation of a Board object. """
        s = ''
        for row in range(len(self.tiles)):
            for col in range(len(self.tiles[0])):
                if self.tiles[row][col] == 0:
                    s += '_ '
                else:
                    s += str(self.tiles[row][col]) + ' '
            s += '\n'
        return s

    def move_blank(self, direction):
        """ Takes as input a string direction that specifies the direction
            in which the blank should move. """
        if direction == 'up':
            new_blank_row = self.blank_r - 1
            new_blank_col = self.blank_c
        elif direction == 'down':
            new_blank_row = self.blank_r + 1
            new_blank_col = self.blank_c
        elif direction == 'right':
            new_blank_row = self.blank_r
            new_blank_col = self.blank_c + 1
        elif direction == 'left':
            new_blank_row = self.blank_r
            new_blank_col = self.blank_c - 1
        else:
            print('ERROR!!!')
            return False
        if new_blank_col >= len(self.tiles[0]):
            return False
        elif new_blank_row >= len(self.tiles):
            return False
        elif new_blank_row < 0 or new_blank_col < 0:
            return False
        else:
            self.tiles[self.blank_r][self.blank_c] = self.tiles[new_blank_row][new_blank_col]
            self.blank_r = new_blank_row
            self.blank_c = new_blank_col
            self.tiles[new_blank_row][new_blank_col] = 0
            return True

    def digit_string(self):
        """ creates and returns a string of digits that corresponds to the current contents of the
            tiles attribute. """
        b = ''
        for row in range(len(self.tiles)):
            for col in range(len(self.tiles[0])):
                if self.tiles[row][col] == '_':
                    b += '0'
                else:
                    b += str(self.tiles[row][col])
        self.digitstr = b
        return self.digitstr

    def copy(self):
        """ returns a newly-constructed Board object that is a deep copy of the called object. """
        new_self = [[0] * 3 for x in range(3)]
        b = ''
        for row in range(len(self.tiles)):
            for col in range(len(self.tiles[0])):
                b += str(self.tiles[row][col])
        new_object = Board(b)    
        return new_object
        
    def num_misplaced(self):
        """ counts and returns the number of tiles in the called Board object that are
            not where they should be in the goal state.  """
        count = 0
        solved_board = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
        
        for row in range(len(self.tiles)):
            for col in range(len(self.tiles[0])):
                if row == 0 and col == 0:
                    count += 0
                elif self.tiles[row][col] != solved_board[row][col]:
                    count += 1
        return count

    def distance(self):
        count = 0
        solved_board = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
        
        for row in range(len(self.tiles)):
            for col in range(len(self.tiles[0])):
                n = self.tiles[row][col]
                count += (abs(row - (n // 3)) + abs(col - n % 3))
        return count
        
    def __eq__(self, other):
        """ returns True if self and objects have the same attribute, and false otherwise. """
        if self.tiles == other.tiles:
            return True
        else:
            return False
