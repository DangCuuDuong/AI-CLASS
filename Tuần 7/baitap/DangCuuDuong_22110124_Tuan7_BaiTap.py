import tkinter as tk
import threading
from collections import deque
from tkinter import messagebox
class Puzzle:
    def __init__(self,board, parent = None, move=""):
        self.board = board
        self.parent = parent
        self.move = move
    def __eq__(self,other):
        return self.board == other.board
    def __hash__(self):
        return hash(self.board)
    def find_zero(self):
        for i in range(len(self.board)):
            if 0 in self.board[i]:
                return i
    def generate_moves(self):
        i,j = self.find_zero()
        possible_moves = []
        if i>0:
            possible_moves.append("UP")
        if i < 2:
            possible_moves.append("DOWN")
        if j > 0:
            possible_moves.append("LEFT")
        if j < 2:
            possible_moves.append("RIGHT")
        return possible_moves
    def apply_move(self,move):
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
        return Puzzle(new_board, self, move)
def bfs(start,goal):
    visited = set()
    queue = deque([start])
    while queue:
        current_state = queue.popleft()
        visited.add(current_state)
        if current_state == goal.board:
            return get_solution(current_state)
        for move in current_state.generate_moves(move):
            new_state = current_state.apply_move(move)
            if new_state not in visited:
                queue.append(new_state)
    return None
def dfs(start,goal):
    stack =[(start,0)]
    visited = set()
    while stack:
        current_state, depth = stack.pop()
        visited.add(current_state)
        if current_state.board == goal.board:
            return get_solution(current_state)
    return None
def get_solution(state):
    moves = []
    while state.parent is not None:
        moves.append(state.move)
        state = state.parent
    return moves[::-1]
def color(board,labels):
    colors = ["white", "light blue", "light green", "light pink", "yellow", "orange", "light grey", "light coral", "light cyan"]
    for i in range(3):
        for j in range(3):
            labels[i][j].config(text=str(board[i][j]) if board[i][j] != 0 else "", bg=colors[board[i][j]])
def solve_with_bfs():
    global step_count
    step_count = 0
    solution = bfs(start,goal)
    if solution:
        apply_moves_gui(solution)
    else:
         messagebox.showinfo("No solution found")            
def solve_with_dfs():
    global step_count
    step_count = 0
    solution = dfs(start,goal)
    if solution:
        apply_moves_gui(solution)
    else:
         messagebox.showinfo("No solution found")     
def apply_moves_gui(solution):
    if solution:
        move = solution.pop(0)
        apply_move_gui(move)
        root.after(500, lambda: apply_moves_gui(solution)) 
    else:
        messagebox.showinfo("Completed", f"Puzzle solved in {step_count} steps!")
def apply_move_gui(move):
    global state, step_count
    start = start.apply_move(move)
    step_count += 1
    step_label.config(text=f"Steps: {step_count}")
    color(start.board,board_labels)
def solve_with_bfs_threaded():
    thread = threading.Thread(target=solve_with_bfs)
    thread.start()
def restart_puzzle():
    global start,  step_count
    start_state = Puzzle([[2, 6, 5], [8, 7, 0], [4, 3, 1]])
    step_count = 0
    step_label.config(text="Steps: 0")
    color(start.board, board_labels)
root = tk.Tk()
root.title("8-Puzzle Solver")
root.geometry("2000x1000")
root.config(bg="light yellow")
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

start= Puzzle([[2, 6, 5], [8, 7, 0], [4, 3, 1]])
goal= Puzzle([[1, 2, 3], [4, 5, 6], [7, 8, 0]])
color(start.board, board_labels)

step_count = 0

root.mainloop()


#Link https://drive.google.com/file/d/1ByDFeTJNnfFF85p4Y5S8RBXlbrgkg6CB/view?usp=drive_link