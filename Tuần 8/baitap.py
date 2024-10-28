import heapq

# Lưu trữ cost cho từng bước di chuyển
MOVE_COST = {
    'UP': 2, 
    'DOWN': 2, 
    'LEFT': 1, 
    'RIGHT': 1
}

# state vị trí bắt đầu và kết thúc
start_state = [2, 8, 3, 1, 6, 4, 7, 0, 5]
goal_state = [1, 2, 3, 8, 0, 4, 7, 6, 5]

# Tìm ô di chuyển hợp lệ
def possible_moves(state):
    blank_idx = state.index(0)
    moves = []
    
    # Di chuyển lên
    if blank_idx not in [0, 1, 2]:
        new_state = state[:]
        new_state[blank_idx], new_state[blank_idx - 3] = new_state[blank_idx - 3], new_state[blank_idx]
        moves.append(('UP', new_state, MOVE_COST['UP']))
    
    # Di chuyển xuống
    if blank_idx not in [6, 7, 8]:
        new_state = state[:]
        new_state[blank_idx], new_state[blank_idx + 3] = new_state[blank_idx + 3], new_state[blank_idx]
        moves.append(('DOWN', new_state, MOVE_COST['DOWN']))
    
    # Di chuyển trái
    if blank_idx not in [0, 3, 6]:
        new_state = state[:]
        new_state[blank_idx], new_state[blank_idx - 1] = new_state[blank_idx - 1], new_state[blank_idx]
        moves.append(('LEFT', new_state, MOVE_COST['LEFT']))
    
    # Di chuyển phải
    if blank_idx not in [2, 5, 8]:
        new_state = state[:]
        new_state[blank_idx], new_state[blank_idx + 1] = new_state[blank_idx + 1], new_state[blank_idx]
        moves.append(('RIGHT', new_state, MOVE_COST['RIGHT']))
    
    return moves

# UCS 
def ucs(start_state, goal_state):
    #(min-heap)
    frontier = []
    heapq.heappush(frontier, (0, start_state, []))  # (cost, state, path)
    
    explored = set()
    
    while frontier:
        cost, current_state, path = heapq.heappop(frontier)
        
        # Nếu đã xong
        if current_state == goal_state:
            return path, cost 
        
        # Đánh dấu đường đã tìm
        explored.add(tuple(current_state))
        
        # Tìm các ô xung quanh
        for move, new_state, move_cost in possible_moves(current_state):
            if tuple(new_state) not in explored:
                new_path = path + [move]
                heapq.heappush(frontier, (cost + move_cost, new_state, new_path))
    
    return None, 0

# Chạy thuật toán UCS
solution, total_cost = ucs(start_state, goal_state)

# In kết quả với các bước dịch chuyển ngược lại
if solution:
    print("Solution found:")
    print("Đường di chuyển của ô trống", solution)
    print("kết quả di chuyển của ma trận:")    
    # In kết quả di chuyển của ma trận
    for move in solution:
        if move == "LEFT":
            print("RIGHT")
        elif move == "RIGHT":
            print("LEFT")
        elif move == "UP":
            print("DOWN")
        elif move == "DOWN":
            print("UP")

    print("Total cost:", total_cost)
else:
    print("No solution found")
