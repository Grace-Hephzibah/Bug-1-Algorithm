import pygame
import sys
import time 
from var import *

# INITIALIZE PYGAME
#------------------------
pygame.init()

# SET UP THE DISPLAY
#------------------------
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("BUG 1 ALGORITHM - ROBOTICS")

# DEFINE GRID PROPERTIES
#------------------------
GRID_SIZE = 50
GRID_WIDTH = WIDTH // GRID_SIZE
GRID_HEIGHT = HEIGHT // GRID_SIZE

# ROBOT AND GOAL POSITIONS
#------------------------
robot_pos = None
goal_pos = None

# GRID WITH OBSTACLES
#------------------------ 
obstacles = set()

# TRACKING THE ALGORITHM
#------------------------
running = False

# DRAW THE GRID 
#------------------------
def draw_grid():
    for x in range(0, WIDTH, GRID_SIZE):
        pygame.draw.line(screen, LINES, (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, GRID_SIZE):
        pygame.draw.line(screen, LINES, (0, y), (WIDTH, y))

# DRAW THE OBSTACLES
#-----------------------
def draw_obstacles():
    for obstacle in obstacles:
        pygame.draw.rect(screen, OBSTACLES, (obstacle[0] * GRID_SIZE, obstacle[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))

# DRAW THE ROBOT AND GOAL
#------------------------
def draw_robot_and_goal():
    if robot_pos:
        pygame.draw.rect(screen, ROBOT, (robot_pos[0] * GRID_SIZE, robot_pos[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))
    if goal_pos:
       pygame.draw.rect(screen, GOAL, (goal_pos[0] * GRID_SIZE, goal_pos[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))

# CALCULATING THE DISTANCE BETWEEN THE ROBOT AND THE GOAL
#------------------------
def manhattan_distance(pos):
    x1, y1 = pos
    x2, y2 = goal_pos
    distance = abs(x2-x1) + abs(y2-y1)
    return distance

# MOVING AROUND AN OBSTACLE
#------------------------
def direction(current_pos, obstacle_pos):
    cx, cy = current_pos
    ox, oy = obstacle_pos
    dx, dy = cx-ox, cy-oy

    if dy == -1:
        return TOP
    elif dx == -1:
        return RIGHT
    elif dx == 1:
        return LEFT
    else:
        return BOTTOM
    
def checkpoint(position, direction):
    currx, curry = position
    updx, updy = next_step_dic[direction]
    nextx, nexty = currx+updx , curry+updy
    next = (nextx, nexty)
    return next

def traverse_obstacle(obstacle_pos, current_pos):
    start = current_pos
    obs_direction = direction(current_pos, obstacle_pos)
    travel_dir = obstacle_direction[obs_direction]
    next = checkpoint(current_pos, travel_dir)
    assumed_obstacle = checkpoint(next, obs_direction)
    
    minimum_distance = 100
    past_moves = [current_pos]

    while True:
        time.sleep(1)
        # Updating the display
        pygame.display.update()
        if current_pos != past_moves[-1]:
            past_moves.append(current_pos)

        if next in obstacles:
            obstacle_pos = next 
            obs_direction = direction(current_pos, obstacle_pos)
            travel_dir = obstacle_direction[obs_direction]
            next = checkpoint(current_pos, travel_dir)
            assumed_obstacle = checkpoint(next, obs_direction)
            continue

        elif assumed_obstacle not in obstacles:
            pygame.draw.rect(screen, TRAIL, (current_pos[0] * GRID_SIZE, current_pos[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))
            obs_direction = direction_obstacle[obs_direction]
            travel_dir = obstacle_direction[obs_direction]
            current_pos = next
            temp = manhattan_distance(current_pos)
            if temp<minimum_distance:
                minimum_distance = temp
            next = checkpoint(current_pos, travel_dir)
            assumed_obstacle = obstacle_pos
            pygame.draw.rect(screen, ROBOT, (current_pos[0] * GRID_SIZE, current_pos[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))
            continue
        
        else:
            pygame.draw.rect(screen, TRAIL, (current_pos[0] * GRID_SIZE, current_pos[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))
            temp = manhattan_distance(current_pos)
            if temp<minimum_distance:
                minimum_distance = temp
            current_pos = next
            obstacle_pos = assumed_obstacle
            next = checkpoint(current_pos, travel_dir)
            assumed_obstacle = checkpoint(next, obs_direction)
            pygame.draw.rect(screen, ROBOT, (current_pos[0] * GRID_SIZE, current_pos[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))

        if start == current_pos:
            break

    i=0
    while True:
        time.sleep(1)
        # Updating the display
        pygame.display.update()

        pygame.draw.rect(screen, TRAIL, (current_pos[0] * GRID_SIZE, current_pos[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))
        if manhattan_distance(current_pos) == minimum_distance:
            return current_pos
        i+=1
        current_pos = past_moves[i]
        pygame.draw.rect(screen, ROBOT, (current_pos[0] * GRID_SIZE, current_pos[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))
         

# INSTRUCTIONS TO MOVE FORWARD
#------------------------
def move_towards_goal():
    global robot_pos
    if robot_pos == goal_pos:
        return
    x, y = robot_pos
    pygame.draw.rect(screen, TRAIL, (robot_pos[0] * GRID_SIZE, robot_pos[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))
    goal_x, goal_y = goal_pos

    if x < goal_x:
        x += 1
    elif x > goal_x:
        x -= 1
    elif y < goal_y:
        y += 1
    elif y > goal_y:
        y -= 1

    if (x,y) in obstacles:
        robot_pos = traverse_obstacle(obstacle_pos=(x,y), current_pos=robot_pos)
    else:
        robot_pos = (x, y)

    pygame.draw.rect(screen, ROBOT, (robot_pos[0] * GRID_SIZE, robot_pos[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))
    return True


# DEFINING THE ALGORITHM
#------------------------
def bug1_algorithm():
    global robot_pos, goal_pos, running
    while robot_pos != goal_pos:

        if not running:
            return
        
        state = move_towards_goal()
        if state == False:
            return 
        
        time.sleep(1)

        # Updating the display
        pygame.display.update()

# MAIN LOOP
#------------------------
while True:
    # Screen display color
    screen.fill(BACKGROUND)

    # Initializing the screen 
    draw_grid()
    draw_obstacles()
    draw_robot_and_goal()

    # Handling events
    for event in pygame.event.get():

        # Exiting the game 
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Setting the robot, goal and obstacles
        elif event.type == pygame.MOUSEBUTTONDOWN and not running:
            x, y = event.pos
            x //= GRID_SIZE
            y //= GRID_SIZE
            if (x, y) not in obstacles:
                if robot_pos is None:
                    robot_pos = (x, y)
                elif goal_pos is None:
                    goal_pos = (x, y)
                else:
                    obstacles.add((x, y))

        # Starting the algorithm
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and robot_pos and goal_pos:
                running = True
                bug1_algorithm()
                time.sleep(10)

    # Updating the display
    pygame.display.update()