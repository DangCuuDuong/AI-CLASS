import pygame
import sys

pygame.init()

# Set up cửa sổ trò chơi
screen_width, screen_height = 1500, 750
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Maze Game")

# Load images and scale them
bg = pygame.transform.scale(pygame.image.load(r'C:\Users\DELL\OneDrive\Desktop\AI\gamemecung\gamemecung\green-fake-grass-background.jpg'), (screen_width, screen_height))
wall = pygame.transform.scale(pygame.image.load(r'C:\Users\DELL\OneDrive\Desktop\AI\gamemecung\gamemecung\brick-wall-texture.jpg'), (30, 30))
rabbit = pygame.transform.scale(pygame.image.load(r'C:\Users\DELL\OneDrive\Desktop\AI\gamemecung\gamemecung\contho.png'), (40, 40))
cave = pygame.transform.scale(pygame.image.load(r'C:\Users\DELL\OneDrive\Desktop\AI\gamemecung\gamemecung\cave.png'), (40, 40))

# Define colors and font
WHITE = (255, 255, 255)
font = pygame.font.SysFont("timesnewroman", 48)

# Mê cung, 1 là tường, 0 là ô trống
maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1],
    [1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1],
    [1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1],
    [1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1],
    [1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1],
    [1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1],
    [1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1],
    [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

# Function to initialize the positions of rabbit and cave
def initialize_positions(maze, start_x, start_y):
    def find_position(row_idx):
        for col in range(len(maze[row_idx])):
            if maze[row_idx][col] == 0:
                return (start_x + col * tile_size + tile_size, start_y + row_idx * tile_size + tile_size)

    rabbit_pos = find_position(0)
    cave_pos = find_position(len(maze) - 1)
    
    rabbit_rect = rabbit.get_rect(center=(rabbit_pos[0], rabbit_pos[1] - 30))
    cave_rect = cave.get_rect(center=(cave_pos[0], cave_pos[1] + 20))
    return rabbit_rect, cave_rect

# Function to draw maze
def draw_maze(maze, start_x, start_y):
    for row in range(len(maze)):
        for col in range(len(maze[row])):
            if maze[row][col] == 1:
                screen.blit(wall, (start_x + col * tile_size, start_y + row * tile_size))

# Function to draw button text
def draw_button_text(text, x, y, text_color):
    label = font.render(text, True, text_color)
    screen.blit(label, (x, y))

# Calculate positions for the maze
tile_size = 25
maze_width, maze_height = len(maze[0]) * tile_size, len(maze) * tile_size
gap_between_mazes = 300

# Position maze 1 and maze 2
start_x1, start_y1 = (screen_width // 2) - maze_width - (gap_between_mazes // 2), (screen_height - maze_height) // 2
start_x2, start_y2 = (screen_width // 2) + (gap_between_mazes // 2), start_y1

# Game state variables
start_time = pygame.time.get_ticks()
rabbit_rect1, cave_rect1 = initialize_positions(maze, start_x1, start_y1)
rabbit_rect2, cave_rect2 = initialize_positions(maze, start_x2, start_y2)

buttons = {"Reset": (50, screen_height - 60, 120, 50)}

# Main game loop
while True:
    screen.blit(bg, (0, 0))  # Draw background

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    # Draw line separating two mazes
    pygame.draw.line(screen, WHITE, (screen_width // 2, 0), (screen_width // 2, screen_height), 5)

    # Draw both mazes with rabbit and cave
    for (rect_rabbit, rect_cave, x, y) in [(rabbit_rect1, cave_rect1, start_x1, start_y1), 
                                           (rabbit_rect2, cave_rect2, start_x2, start_y2)]:
        draw_maze(maze, x, y)
        screen.blit(rabbit, rect_rabbit)
        screen.blit(cave, rect_cave)

    # Update and display timer
    timer = (pygame.time.get_ticks() - start_time) // 1000
    timer_text = font.render(f"Time: {timer}", True, WHITE)
    screen.blit(timer_text, (10, 10))

    # Draw buttons
    for button, (x, y, width, height) in buttons.items():
        draw_button_text(button, x, y, WHITE)

    pygame.display.update()

# Thành viên nhóm:
# 22110124	Đặng Cửu Dương
# 22110117	Lê Thị Mỹ Dung
# 22110250	Nguyễn Phạm Nhật Trân
#LINK VIDEO: 
