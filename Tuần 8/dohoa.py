import tkinter as tk
import heapq

# Kích thước của lưới (3x3)
SIZE = 3
TILE_SIZE = 150  # Increase tile size for better visibility

# Goal state
start_state =[2,8,3,1,6,4,7,0,5]
goal_state =[1,2,3,8,0,4,7,6,5]

MOVE_COST = {
    'UP': 2,
    'DOWN': 2,
    'LEFT': 1,
    'RIGHT': 1
}

def get_possible_moves(state):
    blank_idx = state.index(0)
    moves = []
    
    # UP
    if blank_idx not in [0, 1, 2]:
        new_state = state[:]
        new_state[blank_idx], new_state[blank_idx - 3] = new_state[blank_idx - 3], new_state[blank_idx]
        moves.append(('UP', new_state, MOVE_COST['UP']))
        
    # DOWN
    if blank_idx not in [6, 7, 8]:
        new_state = state[:]
        new_state[blank_idx], new_state[blank_idx + 3] = new_state[blank_idx + 3], new_state[blank_idx]
        moves.append(('DOWN', new_state, MOVE_COST['DOWN']))
        
    # LEFT
    if blank_idx not in [0, 3, 6]:
        new_state = state[:]
        new_state[blank_idx], new_state[blank_idx - 1] = new_state[blank_idx - 1], new_state[blank_idx]
        moves.append(('LEFT', new_state, MOVE_COST['LEFT']))
        
    # RIGHT
    if blank_idx not in [2, 5, 8]:
        new_state = state[:]
        new_state[blank_idx], new_state[blank_idx + 1] = new_state[blank_idx + 1], new_state[blank_idx]
        moves.append(('RIGHT', new_state, MOVE_COST['RIGHT']))
        
    return moves

# UCS algorithm
def uniform_cost_search(start_state, goal_state):
    frontier = []
    heapq.heappush(frontier, (0, start_state, []))  # (cost, state, path)
    
    explored = set()
    
    while frontier:
        cost, current_state, path = heapq.heappop(frontier)
        
        if current_state == goal_state:
            return path, cost  # Return the path and the total cost
        
        explored.add(tuple(current_state))
        
        for move, new_state, move_cost in get_possible_moves(current_state):
            if tuple(new_state) not in explored:
                new_path = path + [move]
                heapq.heappush(frontier, (cost + move_cost, new_state, new_path))
    
    return None, 0

# GUI with Tkinter
class PuzzleGUI:
    def __init__(self, root, state):
        self.root = root
        self.state = state
        
        self.canvas = tk.Canvas(root, width=SIZE * TILE_SIZE, height=SIZE * TILE_SIZE)
        self.canvas.pack()

        # Labels to display moves and cost
        self.moves_label = tk.Label(root, text="Moves: ")
        self.moves_label.pack()
        
        self.cost_label = tk.Label(root, text="Cost: ")
        self.cost_label.pack()

        # Colors for the numbered tiles
        self.tile_colors = {
            1: "lightgreen",
            2: "lightcoral",
            3: "lightcyan",
            4: "lightpink",
            5: "lightyellow",
            6: "lightblue",
            7: "lightsalmon",
            8: "lightgoldenrod",
            0: "white"  # Blank tile
        }

        # Initialize puzzle tiles
        self.tiles = []
        self.draw_puzzle()

    def draw_puzzle(self):
        """Draw the puzzle tiles based on the current state."""
        self.canvas.delete("all")
        for i in range(SIZE):
            for j in range(SIZE):
                idx = i * SIZE + j
                value = self.state[idx]
                tile_color = self.tile_colors[value]
                
                tile = self.canvas.create_rectangle(
                    j * TILE_SIZE, i * TILE_SIZE, 
                    (j + 1) * TILE_SIZE, (i + 1) * TILE_SIZE,
                    fill=tile_color, outline="black"
                )
                if value != 0:
                    self.canvas.create_text(
                        j * TILE_SIZE + TILE_SIZE // 2, 
                        i * TILE_SIZE + TILE_SIZE // 2,
                        text=str(value),
                        font=("Arial", 36)  # Increased font size for better visibility
                    )

    def update_puzzle(self, state):
        """Update the puzzle with a new state."""
        self.state = state
        self.draw_puzzle()

    def solve_puzzle(self):
        """Solve the puzzle and display moves and cost."""
        solution, total_cost = uniform_cost_search(self.state, goal_state)
        if solution:
            # Display moves and total cost
            self.moves_label.config(text=f"Moves: {', '.join(solution)}")
            self.cost_label.config(text=f"Total Cost: {total_cost}")
            self.animate_solution(solution)
        else:
            self.moves_label.config(text="No solution found")
            self.cost_label.config(text="")

    def animate_solution(self, solution):
        """Animate the steps of the solution."""
        def make_move(step_idx):
            if step_idx >= len(solution):
                return
            move = solution[step_idx]
            self.state = self.apply_move(self.state, move)
            self.update_puzzle(self.state)
            self.root.after(500, make_move, step_idx + 1)
        make_move(0)

    def apply_move(self, state, move):
        """Apply a move (UP, DOWN, LEFT, RIGHT) to the current state."""
        blank_idx = state.index(0)
        if move == 'UP':
            new_blank_idx = blank_idx - 3
        elif move == 'DOWN':
            new_blank_idx = blank_idx + 3
        elif move == 'LEFT':
            new_blank_idx = blank_idx - 1
        elif move == 'RIGHT':
            new_blank_idx = blank_idx + 1
        new_state = state[:]
        new_state[blank_idx], new_state[new_blank_idx] = new_state[new_blank_idx], new_state[blank_idx]
        return new_state

# Run the GUI
def main():
    root = tk.Tk()
    root.title("8-Puzzle Solver")
    
    puzzle_gui = PuzzleGUI(root, start_state)
    
    # Solve button
    solve_button = tk.Button(root, text="Solve", command=puzzle_gui.solve_puzzle)
    solve_button.pack()
    
    root.mainloop()

if __name__ == "__main__":
    main()
