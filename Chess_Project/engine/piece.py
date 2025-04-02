# Logic for chess pieces

class Piece:
    """
    מחלקה שמייצגת כלי שחמט.
    """
    def __init__(self, color, type):
        self.color = color
        self.type = type

    def __repr__(self):
        return f"{self.color} {self.type}"

    def valid_moves(self, board, start_pos):
        """
        מחזיר את כל המהלכים החוקיים לכלי.
        """
        moves = []
        row, col = start_pos[0], start_pos[1] # Correct start_pos usage
        if self.type == "pawn":
            # לוגיקה לרגלי
            direction = -1 if self.color == "white" else 1
            new_col = col + direction
            if 0 <= new_col < 8:
                # תנועה קדימה
                if board[row][new_col] is None:
                    moves.append((row, new_col))
                # תקיפה באלכסון
                if row > 0 and board[row - 1][new_col] is not None and board[row - 1][new_col][0] != self.color:
                    moves.append((row - 1, new_col))
                if row < 7 and board[row + 1][new_col] is not None and board[row + 1][new_col][0] != self.color:
                    moves.append((row + 1, new_col))
        elif self.type == "knight":
            # לוגיקה לפרש
            knight_moves = [
                (-2, -1), (-2, 1), (-1, -2), (-1, 2),
                (1, -2), (1, 2), (2, -1), (2, 1)
            ]
            for move in knight_moves:
                new_row, new_col = row + move[0], col + move[1]
                if 0 <= new_row < 8 and 0 <= new_col < 8:
                    if board[new_row][new_col] is None or board[new_row][new_col][0] != self.color:
                        moves.append((new_row, new_col))
        # המשך לוגיקה לכל כלי
        return moves
