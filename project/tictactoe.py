def display_board(board):
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")

def check_winner(board, player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Baris
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Kolom
        [0, 4, 8], [2, 4, 6]              # Diagonal
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False

def is_draw(board):
    return all(space != ' ' for space in board)

def make_move(board, player):
    while True:
        try:
            move = int(input(f"Pemain {player}, masukkan nomor posisi (1-9): ")) - 1
            if move < 0 or move > 8:
                print("Nomor posisi harus antara 1-9.")
            elif board[move] != ' ':
                print("Posisi ini sudah ditempati. Pilih posisi lain.")
            else:
                board[move] = player
                break
        except ValueError:
            print("Masukkan angka yang valid.")

def play_game():
    board = [' '] * 9
    current_player = 'X'
    print("Selamat datang di Tic-Tac-Toe!")
    display_board(board)

    while True:
        make_move(board, current_player)
        display_board(board)

        if check_winner(board, current_player):
            print(f"Selamat! Pemain {current_player} menang!")
            break
        elif is_draw(board):
            print("Permainan berakhir dengan seri!")
            break

        # Bergantian pemain
        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    play_game()