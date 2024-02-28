# Bug 1 Algorithm 

## About 
Perhaps the most straightforward path planning approach is to move toward the goal, unless an obstacle is encountered, in which case, circumnavigate the obstacle 
until motion toward the goal is once again allowable. Essentially, the Bug1 algorithm formalizes the “common sense” idea of moving toward the goal and going around obstacles.

_Thanks to <a href = "https://www.cs.columbia.edu/~allen/F19/NOTES/howie_errata.pdf"> CS Columbia </a>_

_Check out more from <a href = "https://robotics.caltech.edu/wiki/images/e/e1/BugSlides.pdf"> Robotics Caltech </a>_

## Basic Assumptions 
- The robot is treated as a point inside a 2D world.
- The obstacles (if any) are unknown and non-convex.
- Clearly defined starting point and goal.
- The robot can detect obstacle boundaries from a distance of known length.
- The robot always knows the direction and how far (in terms of Euclidean distance) it is from the goal.
  
_Thanks to <a href = "https://en.wikipedia.org/wiki/Bug_algorithm"> Wikipedia </a>_

## Algorithm 
- The robot moves towards the goal until an obstacle is encountered.
- Follow a canonical direction (clockwise) until the robot reaches the location of the initial encounter with the obstacle (in short, walking around the obstacle).
- The robot then follows the obstacle's boundary to reach the point on the boundary that is closest to the goal.
- Go back to step 1. Repeat this until the goal is reached.

_Thanks to <a href = "https://en.wikipedia.org/wiki/Bug_algorithm"> Wikipedia </a>_

## Working Demo 
- The first click on the grid shows the initial position of the robot in the environment
- The second click on the grid shows the goal position that the robot will attempt to reach. 
- The rest of the clicks will create obstacles.
- Finally, once the environment is custom-created, click the space bar to see the algorithm in action.

<video width="100" height="100" src="https://github.com/Grace-Hephzibah/tangent-1-algorithm/assets/63595093/9a76b6ec-701d-472e-bd56-3e195061b650"></video>


