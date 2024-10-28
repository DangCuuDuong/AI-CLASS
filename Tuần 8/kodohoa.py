import heapq

# BoardNode class represents each state of the puzzle
class BoardNode:
    def __init__(self, state, parent=None, move=None, cost=0):
        self.state = state
        self.parent = parent
        self.move = move
        self.cost = cost  # g(n), the cost to reach this node

    def get_max_cost(self):
        return self.cost

    def is_goal(self, goal_state):
        return self.state == goal_state

    def hash_code(self):
        return hash(tuple(self.state))

# Info class to manage priority queue and visited states
class Info:
    def __init__(self):
        self.pQueue = []  # Priority Queue
        self.visited = {}  # To track visited nodes
        self.time = 0  # To count the number of expansions

    def make_pqueue(self):
        self.pQueue = []

    def inc_time(self):
        self.time += 1

# gComparator is integrated as the heapq in Python works natively with sorting by cost
def g_comparator(node):
    return node.get_max_cost()

# PathActions class for printing the path from initial state to goal state
class PathActions:
    def __init__(self, initial_node, goal_node, info):
        self.initial_node = initial_node
        self.goal_node = goal_node
        self.info = info

    def get_path(self):
        path = []
        node = self.goal_node
        while node:
            if node.move:
                path.append(node.move)
            node = node.parent
        return path[::-1]  # Reverse path to go from start to goal

    def print_path(self):
        path = self.get_path()
        print(f"Path to goal: {path}")
        print(f"Cost: {self.goal_node.get_max_cost()}")

# Successor class to generate successors (new states) for a given state
class Successor:
    def __init__(self):
        pass

    def successor(self, node):
        successors = []
        zero_index = node.state.index(0)

        # Define moves for the 8-puzzle
        moves = [('UP', -3), ('DOWN', 3), ('LEFT', -1), ('RIGHT', 1)]
        valid_moves = self.get_valid_moves(zero_index, moves)

        for move, move_offset in valid_moves:
            new_state = node.state[:]
            swap_index = zero_index + move_offset
            new_state[zero_index], new_state[swap_index] = new_state[swap_index], new_state[zero_index]
            cost = node.get_max_cost() + (2 if move in ['UP', 'DOWN'] else 1)
            successors.append(BoardNode(new_state, node, move, cost))

        return successors

    def get_valid_moves(self, index, moves):
        valid_moves = []
        for move, offset in moves:
            if self.is_valid_move(index, move):
                valid_moves.append((move, offset))
        return valid_moves

    def is_valid_move(self, zero_index, direction):
        if direction == 'UP' and zero_index >= 3:
            return True
        if direction == 'DOWN' and zero_index <= 5:
            return True
        if direction == 'LEFT' and zero_index % 3 != 0:
            return True
        if direction == 'RIGHT' and zero_index % 3 != 2:
            return True
        return False

# UniformCost class implements the UCS algorithm
class UniformCost:
    def __init__(self, initial_node, goal_state):
        self.initial_node = initial_node
        self.goal_state = goal_state

    def search(self):
        # Create priority queue sorted by g(n) using heapq
        info = Info()
        heapq.heappush(info.pQueue, (self.initial_node.get_max_cost(), self.initial_node))

        while info.pQueue:
            _, node = heapq.heappop(info.pQueue)
            info.inc_time()
            info.visited[node.hash_code()] = node

            if node.is_goal(self.goal_state):
                path = PathActions(self.initial_node, node, info)
                path.print_path()  # Print the solution path
                return True

            successor_generator = Successor()
            successors = successor_generator.successor(node)

            for temp_node in successors:
                if temp_node.hash_code() not in info.visited:
                    heapq.heappush(info.pQueue, (temp_node.get_max_cost(), temp_node))

        return False  # Return false if no solution is found

# Example usage
if __name__ == "__main__":
    # Define start and goal states
    start_state = [2, 8, 3, 1, 6, 4, 7, 0, 5]
    goal_state = [1, 2, 3, 8, 0, 4, 7, 6, 5]

    # Create the initial node
    initial_node = BoardNode(start_state)

    # Perform UCS search
    ucs = UniformCost(initial_node, goal_state)
    ucs.search()
