import tkinter as tk
import threading
from collections import deque
from tkinter import messagebox

class PuzzleState:
    def __init__(self, board, parent=None, move=""):
        self.board = board
        self.parent = parent
        self.move = move

    def __eq__(self, other):
        return self.board == other.board

    def __hash__(self):
        return hash(str(self.board))

    def find_zero(self):
        for i in range(len(self.board)):
            if 0 in self.board[i]:
                return i, self.board[i].index(0)

    def generate_moves(self):
        i, j = self.find_zero()
        possible_moves = []
        if i > 0:
            possible_moves.append("UP")
        if i < 2:
            possible_moves.append("DOWN")
        if j > 0:
            possible_moves.append("LEFT")
        if j < 2:
            possible_moves.append("RIGHT")
        return possible_moves

    def apply_move(self, move):
        i, j = self.find_zero()
        new_board = [row[:] for row in self.board]
        if move == "UP":
            new_board[i][j], new_board[i-1][j] = new_board[i-1][j], new_board[i][j]
        elif move == "DOWN":
            new_board[i][j], new_board[i+1][j] = new_board[i+1][j], new_board[i][j]
        elif move == "LEFT":
            new_board[i][j], new_board[i][j-1] = new_board[i][j-1], new_board[i][j]
        elif move == "RIGHT":
            new_board[i][j], new_board[i][j+1] = new_board[i][j+1], new_board[i][j]
        return PuzzleState(new_board, self, move)

def bfs(start_state, goal_state):
    visited = set()
    queue = deque([start_state])

    while queue:
        current_state = queue.popleft()
        visited.add(current_state)

        if current_state.board == goal_state.board:
            return get_solution(current_state)

        for move in current_state.generate_moves():
            new_state = current_state.apply_move(move)
            if new_state not in visited:
                queue.append(new_state)

    return None

def dfs(start_state, goal_state, depth_limit=50):
    stack = [(start_state, 0)]
    visited = set()

    while stack:
        current_state, depth = stack.pop()
        visited.add(current_state)

        if current_state.board == goal_state.board:
            return get_solution(current_state)

        if depth < depth_limit:
            for move in current_state.generate_moves():
                new_state = current_state.apply_move(move)
                if new_state not in visited:
                    stack.append((new_state, depth + 1))

    return None

def get_solution(state):
    moves = []
    while state.parent is not None:
        moves.append(state.move)
        state = state.parent
    return moves[::-1]

def update_board_gui(board, labels):
    colors = ["white", "light blue", "light green", "light pink", "yellow", "orange", "light grey", "light coral", "light cyan"]
    for i in range(3):
        for j in range(3):
            labels[i][j].config(text=str(board[i][j]) if board[i][j] != 0 else "", bg=colors[board[i][j]])

def solve_with_bfs():
    global step_count
    step_count = 0
    solution = bfs(start_state, goal_state)
    if solution:
        apply_moves_gui(solution)
    else:
        print("No solution found")

def solve_with_dfs():
    global step_count
    step_count = 0
    solution = dfs(start_state, goal_state)
    if solution:
        apply_moves_gui(solution)
    else:
        print("No solution found")

def apply_moves_gui(solution):
    if solution:
        move = solution.pop(0)
        apply_move_gui(move)
        root.after(500, lambda: apply_moves_gui(solution))  # Delay 500ms between moves
    else:
        messagebox.showinfo("Completed", f"Puzzle solved in {step_count} steps!")

def apply_move_gui(move):
    global start_state, step_count
    start_state = start_state.apply_move(move)
    step_count += 1
    step_label.config(text=f"Steps: {step_count}")
    update_board_gui(start_state.board, board_labels)

def solve_with_bfs_threaded():
    thread = threading.Thread(target=solve_with_bfs)
    thread.start()

def restart_puzzle():
    global start_state, step_count
    start_state = PuzzleState([[2, 6, 5], [8, 7, 0], [4, 3, 1]])  # Reset to initial state
    step_count = 0
    step_label.config(text="Steps: 0")
    update_board_gui(start_state.board, board_labels)

# GUI Initialization
root = tk.Tk()
root.title("8-Puzzle Solver")
root.geometry("2000x1000")  # Set window size
root.config(bg="light yellow")  # Set background color

frame = tk.Frame(root, bg="light yellow")
frame.pack()

board_labels = [[None for _ in range(3)] for _ in range(3)]
for i in range(3):
    for j in range(3):
        board_labels[i][j] = tk.Label(frame, text="", width=8, height=5, font=("Arial", 25), borderwidth=2, relief="solid", bg="white")
        board_labels[i][j].grid(row=i, column=j)

step_label = tk.Label(root, text="Steps: 0", font=("Arial", 20), bg="light yellow")
step_label.pack()

bfs_button = tk.Button(root, text="Solve with BFS", font=("Arial", 15), command=solve_with_bfs_threaded, bg="light blue")
bfs_button.pack(pady=10)

dfs_button = tk.Button(root, text="Solve with DFS", font=("Arial", 15), command=lambda: solve_with_dfs(), bg="light green")
dfs_button.pack(pady=10)

restart_button = tk.Button(root, text="Restart", font=("Arial", 15), command=restart_puzzle, bg="orange")
restart_button.pack(pady=10)

start_state = PuzzleState([[2, 6, 5], [8, 7, 0], [4, 3, 1]])
goal_state = PuzzleState([[1, 2, 3], [4, 5, 6], [7, 8, 0]])
update_board_gui(start_state.board, board_labels)

step_count = 0
import random

def shuffle_puzzle():
    global start_state
    # Flatten the board and shuffle it
    flattened_board = [num for row in start_state.board for num in row]
    random.shuffle(flattened_board)
    # Recreate the 3x3 matrix
    new_board = [flattened_board[i:i+3] for i in range(0, 9, 3)]
    start_state = PuzzleState(new_board)
    update_board_gui(start_state.board, board_labels)

def move_puzzle(event):
    global start_state, step_count
    move_map = {'w': 'UP', 's': 'DOWN', 'a': 'LEFT', 'd': 'RIGHT'}
    move = move_map.get(event.char.lower())
    if move and move in start_state.generate_moves():
        start_state = start_state.apply_move(move)
        step_count += 1
        step_label.config(text=f"Steps: {step_count}")
        update_board_gui(start_state.board, board_labels)

# Adding a button for shuffling the puzzle
shuffle_button = tk.Button(root, text="Randomize Puzzle", font=("Arial", 15), command=shuffle_puzzle, bg="light coral")
shuffle_button.pack(pady=10)

# Binding the W, A, S, D keys to move the puzzle
root.bind("<Key>", move_puzzle)


root.mainloop()
