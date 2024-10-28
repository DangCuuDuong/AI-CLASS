import tkinter as tk
from queue import PriorityQueue
from tkinter import messagebox

WIDTH = 600
ROWS = 10  
COLORS = {
    "start": "green",
    "end": "red",
    "obstacle": "black",
    "path": "cyan",
    "open": "yellow",
    "closed": "orange",
    "default": "white"
}
MAP = ["0000000000","0011100000","0000100000","0000111100","0000100000","0111100000","0010000111","0010000000","0010000000","0000000000"]
class Node:
    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.color = COLORS["default"]
        self.neighbors = []
        self.width = width
        self.total_rows = total_rows
    def get_pos(self):
        return self.row, self.col
    def is_obstacle(self):
        return self.color == COLORS["obstacle"]
    def reset(self):
        self.color = COLORS["default"]
    def make_start(self):
        self.color = COLORS["start"]
    def make_closed(self):
        self.color = COLORS["closed"]
    def make_open(self):
        self.color = COLORS["open"]
    def make_obstacle(self):
        self.color = COLORS["obstacle"]
    def make_end(self):
        self.color = COLORS["end"]
    def make_path(self):
        self.color = COLORS["path"]
    def draw(self, canvas):
        canvas.create_rectangle(
            self.x, self.y, 
            self.x + self.width, self.y + self.width, 
            fill=self.color, outline="grey"
        )

    def update_neighbors(self, grid):
        self.neighbors = []
        directions = [
            (1, 0), (-1, 0), (0, 1), (0, -1), 
            (1, 1), (1, -1), (-1, 1), (-1, -1)
        ]
        for dr, dc in directions:
            r, c = self.row + dr, self.col + dc
            if 0 <= r < self.total_rows and 0 <= c < self.total_rows:
                neighbor = grid[r][c]
                if not neighbor.is_obstacle():
                    self.neighbors.append(neighbor)
def h(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1 - x2) + abs(y1 - y2)
def reconstruct_path(came_from, current, draw):
    steps = 0
    while current in came_from:
        current = came_from[current]
        current.make_path()
        draw()
        steps += 1
    return steps
def a_star(draw, grid, start, end):
    if not start or not end:
        return False
    count = 0
    open_set = PriorityQueue()
    open_set.put((0, count, start))
    came_from = {}
    g_score = {node: float("inf") for row in grid for node in row}
    g_score[start] = 0
    f_score = {node: float("inf") for row in grid for node in row}
    f_score[start] = h(start.get_pos(), end.get_pos())
    open_set_hash = {start}
    while not open_set.empty():
        current = open_set.get()[2]
        open_set_hash.remove(current)
        if current == end:
            steps = reconstruct_path(came_from, end, draw)
            end.make_end()
            messagebox.showinfo("A* SEARCH", f"Path found with {steps} steps!")
            return True
        for neighbor in current.neighbors:
            temp_g_score = g_score[current] + 1
            if temp_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = temp_g_score
                f_score[neighbor] = temp_g_score + h(neighbor.get_pos(), end.get_pos())
                if neighbor not in open_set_hash:
                    count += 1
                    open_set.put((f_score[neighbor], count, neighbor))
                    open_set_hash.add(neighbor)
                    neighbor.make_open()
        draw()
        if current != start:
            current.make_closed()
    messagebox.showinfo("A* SEARCH", "No path found!")
    return False
def make_grid(rows, width):
    grid = []
    gap = width // rows
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            node = Node(i, j, gap, rows)
            if MAP[i][j] == "1":
                node.make_obstacle()
            grid[i].append(node)
    return grid

def draw_grid(canvas, rows, width):
    gap = width // rows
    for i in range(rows):
        canvas.create_line(0, i * gap, width, i * gap)
        canvas.create_line(i * gap, 0, i * gap, width)

def draw(canvas, grid, rows, width):
    canvas.delete("all")
    for row in grid:
        for node in row:
            node.draw(canvas)
    draw_grid(canvas, rows, width)
    canvas.update()
def main():
    app = tk.Tk()
    app.title("A* SEARCH")
    canvas = tk.Canvas(app, width=WIDTH, height=WIDTH)
    canvas.pack()
    grid = make_grid(ROWS, WIDTH)
    start = grid[0][0]  
    end = grid[9][8]   
    start.make_start()
    end.make_end()
    def draw_callback():
        draw(canvas, grid, ROWS, WIDTH)
    draw_callback()
    def start_algorithm():
        for row in grid:
            for node in row:
                node.update_neighbors(grid)
        a_star(lambda: draw(canvas, grid, ROWS, WIDTH), grid, start, end)
    start_button = tk.Button(app, text="Solve", command=start_algorithm)
    start_button.pack()
    app.mainloop()
if __name__ == "__main__":
    main()
