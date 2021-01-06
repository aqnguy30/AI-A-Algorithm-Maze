# AI-A-star-Algorithm-Maze

## Project Description
Solve a maze problem which will find the shortest path in the maze from a start node to the end node using A* algorithm.

## Rules
A* algorithm referenced Patrick Lester’s article:
1. Add the starting square (or node) to the open list.

2. Repeat the following:
A) Look for the lowest F cost square on the open list. We refer to this as the current square.
B). Switch it to the closed list.
C) For each of the 8 squares adjacent to this current square:
If it is not walkable or if it is on the closed list, ignore it. Otherwise do the following.
If it isn’t on the open list, add it to the open list. Make the current square the parent of this square. Record the F, G, and H costs of the square.
If it is on the open list already, check to see if this path to that square is better, using G cost as the measure. A lower G cost means that this is a better path. If so, change the parent of the square to the current square, and recalculate the G and F scores of the square. If you are keeping your open list sorted by F score, you may need to resort the list to account for the change.
D) Stop when you:
Add the target square to the closed list, in which case the path has been found, or
Fail to find the target square, and the open list is empty. In this case, there is no path.

3. Save the path. Working backwards from the target square, go from each square to its parent square until you reach the starting square. That is your path.

## References
https://towardsdatascience.com/a-star-a-search-algorithm-eb495fb156bb
https://medium.com/@nicholas.w.swift/easy-a-star-pathfinding-7e6689c7f7b2

## Author
Tony Nguyen - aqnguy30 - quocanh191997@gmail.com
