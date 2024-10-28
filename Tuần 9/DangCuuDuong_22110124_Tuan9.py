import tkinter as tk
import random
import math
class EightQueens:
    def __init__(self, master):
        self.master = master
        self.canvas = tk.Canvas(self.master, width=400, height=400)
        self.canvas.pack()
        self.solve_button = tk.Button(self.master, text="Solve", command=self.restart)
        self.solve_button.pack(pady=5)
        self.status_label = tk.Label(self.master, text="", fg="green")
        self.status_label.pack(pady=5)
        self.board_size = 8
        self.cell_size = 50
        self.temp = 10000  
        self.cooling_rate = 0.995  
        self.iterations = 1000
        self.state = [random.randint(0, self.board_size - 1) for _ in range(self.board_size)]
        self.draw_board()
    def draw_board(self):
        self.canvas.delete("all")
        for i in range(self.board_size):
            for j in range(self.board_size):
                if (i + j) % 2 == 0: 
                    color = "white" 
                else: 
                    color = "black"
                self.canvas.create_rectangle(j * self.cell_size, i * self.cell_size,(j + 1) * self.cell_size, (i + 1) * self.cell_size, fill=color)

        for i, j in enumerate(self.state):
            self.canvas.create_oval(i * self.cell_size + 5, j * self.cell_size + 5,(i + 1) * self.cell_size - 5, (j + 1) * self.cell_size - 5,fill="red")

    def calculate(self, state):
        conflicts = 0
        for i in range(self.board_size):
            for j in range(i + 1, self.board_size):
                if state[i] == state[j] or abs(state[i] - state[j]) == abs(i - j):
                    conflicts += 1
        return conflicts
    def restart(self):
        self.state = [random.randint(0, self.board_size - 1) for _ in range(self.board_size)]
        self.temp = 10000  
        self.status_label.config(text="") 
        self.simulated_annealing()
    def simulated_annealing(self):
        current_state = self.state[:]
        current_conflicts = self.calculate(current_state)
        while self.temp > 0.1 and current_conflicts > 0:
            for _ in range(self.iterations):
                new_state = current_state[:]
                col = random.randint(0, self.board_size - 1)
                new_state[col] = random.randint(0, self.board_size - 1)
                new_conflicts = self.calculate(new_state)
                delta = new_conflicts - current_conflicts
                if delta < 0 or random.uniform(0, 1)<math.exp(-delta / self.temp):
                    current_state = new_state[:]
                    current_conflicts = new_conflicts
                if current_conflicts == 0:
                    self.status_label.config(text="Solution Found")
                    break
            self.state = current_state[:]
            self.draw_board()
            self.temp *= self.cooling_rate
            self.master.update()
            if current_conflicts == 0:
                self.status_label.config(text="Solution Found")
                break
        else:
            self.status_label.config(text="No solution found.")
root = tk.Tk()
root.title("8-Queens Solver")
root.geometry("400x500")
app = EightQueens(root)
root.mainloop()
#https://drive.google.com/file/d/13il_LH4gOI89Ez7BqfHSCkGASRCPxVms/view?usp=drive_link