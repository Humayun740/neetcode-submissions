class Solution:

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # row check
        for i in range(9):
            seen_set = set()
            seen_list = []
            for j in range(9):
                val = board[i][j]
                if val != ".":
                    seen_set.add(val)
                    seen_list.append(val)
            if len(seen_list) != len(seen_set):
                return False

        # column check
        for i in range(9):
            seen_set = set()
            seen_list = []
            for j in range(9):
                val = board[j][i]
                if val != ".":
                    seen_set.add(val)
                    seen_list.append(val)
            if len(seen_list) != len(seen_set):
                return False

        # cube check
        for row_block in range(0, 9, 3):
            for col_block in range(0, 9, 3):
                seen_set = set()
                seen_list = []
                for i in range(3):
                    for j in range(3):
                        val = board[row_block + i][col_block + j]
                        if val != ".":
                            seen_set.add(val)
                            seen_list.append(val)
                if len(seen_list) != len(seen_set):
                    return False

        return True