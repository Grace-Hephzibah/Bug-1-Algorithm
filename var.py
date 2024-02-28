# DEFINE COLORS
#----------------------
BACKGROUND = (255, 244, 244) # white 
ROBOT = (241, 195, 118) # beige
OBSTACLES = (96, 108, 93) # green
TRAIL = (247, 230, 196) # light beige rgb(247, 230, 196)
LINES = (96, 108, 93) # green 
GOAL = (0, 0, 0) # black 

# DIRECTION NUMBERS
#----------------------
TOP = 0
RIGHT = 1
LEFT = 2
BOTTOM = 3

# ENCODING DICTIONARIES
#----------------------
obstacle_direction = {
    TOP : LEFT, 
    LEFT : BOTTOM, 
    BOTTOM : RIGHT, 
    RIGHT : TOP
}

direction_obstacle = {
    LEFT : TOP, 
    BOTTOM : LEFT, 
    RIGHT : BOTTOM, 
    TOP : RIGHT
}

next_step_dic = {
    LEFT: (-1, 0), 
    RIGHT : (1, 0), 
    TOP : (0, 1), 
    BOTTOM : (0, -1)
}