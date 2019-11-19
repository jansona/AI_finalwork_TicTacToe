

def get_result(board_con) :
    all_line_sums = []
    
    for line in board_con:
        all_line_sums.append(sum(line))
    for j in range(3):
        col_sum = 0
        for i in range(3):
            col_sum += board_con[i][j]
        all_line_sums.append(col_sum)
    slash_line = 0
    back_slash_line = 0
    for i in range(3):
        slash_line += board_con[i][i]
        back_slash_line += board_con[2-i][i]
    all_line_sums.append(slash_line)
    all_line_sums.append(back_slash_line)

    if 3 in all_line_sums:
        return 1
    elif -3 in all_line_sums:
        return -1
    
    for line in board_con:
        if 0 in line:
            return None

    return 0


class MinMaxAlgorithm(object):

    def __init__(self, my_piece=-1, difficult=7) :
        self.my_piece = my_piece
        self.enemy_piece = 0 - my_piece
        self.max_depth = difficult

    def find_avail_action(self) :

        available_action = []

        for i in range(3):
            for j in range(3):
                if self.board_con[i][j] == 0:
                    available_action.append((i, j))
        
        return available_action

    def find_actions(self, pos, piece):
        i, j = pos
        self.board_con[i][j] = piece

    def get_result(self) :
        all_line_sums = []
        
        for line in all_line_sums:
            all_line_sums.append(sum(line))
        for j in range(3):
            col_sum = 0
            for i in range(3):
                col_sum += self.board_con[i][j]
            all_line_sums.append(col_sum)
        slash_line = 0
        back_slash_line = 0
        for i in range(3):
            slash_line += self.board_con[i][i]
            back_slash_line += self.board_con[2-i][i]
        all_line_sums.append(slash_line)
        all_line_sums.append(back_slash_line)

        if 3 in all_line_sums:
            return 1
        elif -3 in all_line_sums:
            return -1
        
        for line in self.board_con:
            if 0 in line:
                return None

        return 0

    def exchange(self, piece) :
        if piece == 1 :
            return -1
        return 1

    def minimax(self, piece, depth=0):

        if depth > self.max_depth:
            return 10 - depth, None
        if piece == self.my_piece: 
            value = -10
        else:
            value = 10
        
        result = get_result(self.board_con)

        if result == self.enemy_piece:
            return -10 + depth, None
        elif result == 0:
            return 0, None
        elif result == self.my_piece:
            return 10 - depth, None

        for action in self.find_avail_action() :
            self.find_actions(action, piece)
            val, _ = self.minimax(self.exchange(piece), depth+1)
            self.find_actions(action, 0)

            # max
            if piece == self.my_piece:
                if val > value:
                    value, suitable_action = val, action
            # min
            else :
                if val < value:
                    value, suitable_action = val, action
                    
        return value, suitable_action

    def __call__(self, board_con):
        self.board_con = board_con
        return self.minimax(self.my_piece)


if __name__ == "__main__":
    board = [[1,0,-1],[0,1,-1],[0,0,0]]

    mma = MinMaxAlgorithm(1)
    print(mma(board))
