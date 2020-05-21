# Anh Quoc Nguyen - PSID: 1596895
import numpy as np


class Node:
    """
        A node class for A* Pathfinding
        parent is parent of the current Node
        position is current position of the Node in the maze
        g is cost from start to current Node
        h is heuristic based estimated cost for current Node to end Node
        f is total cost of present node i.e. :  f = g + h
    """

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position


# This function return the path of the search
def return_path(current_node, maze):
    path = []
    no_rows, no_columns = np.shape(maze)

    # here we create the initialized result maze with -1 in every position
    result = [[-1 for i in range(no_columns)] for j in range(no_rows)]
    current = current_node
    while current is not None:
        path.append(current.position)
        current = current.parent
    # Return reversed path as we need to show from start to end path
    path = path[::-1]
    #start_value = 1
    x_cell = np.arange(1, no_rows * no_columns + 1).reshape(no_rows, -1)
    best_path=[]
    # we update the path of start to end found by A-star search with every step incremented by 1
    for i in range(len(path)):
        #result[path[i][0]][path[i][1]] = x_cell[path[i][0]][path[i][1]]
        best_path.append(x_cell[path[i][0]][path[i][1]])
        #start_value += 1
    #print(x_cell)
    print("Result:", best_path)
    return best_path


def search(maze, cost, start, end):
    """
        Returns a list of tuples as a path from the given start to the given end in the given maze
    """

    # Create start and end node with initized values for g, h and f
    start_node = Node(None, tuple(start))
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, tuple(end))
    end_node.g = end_node.h = end_node.f = 0

    # Initialize both yet_to_visit and visited list
    # in this list we will put all node that are yet_to_visit for exploration.
    # From here we will find the lowest cost node to expand next
    yet_to_visit_list = []
    # in this list we will put all node those already explored so that we don't explore it again
    visited_list = []

    # Add the start node
    yet_to_visit_list.append(start_node)

    # Adding a stop condition. This is to avoid any infinite loop and stop
    # execution after some reasonable number of steps
    outer_iterations = 0
    max_iterations = (len(maze) // 2) ** 10

    # what squares do we search . serarch movement is left-right-top-bottom
    # (4 movements) from every positon

    move = [[-1, 0],  # go up
            [0, -1],  # go left
            [1, 0],  # go down
            [0, 1]]  # go right

    """
        1) We first get the current node by comparing all f cost and selecting the lowest cost node for further expansion
        2) Check max iteration reached or not . Set a message and stop execution
        3) Remove the selected node from yet_to_visit list and add this node to visited list
        4) Perform Goal test and return the path else perform below steps
        5) For selected node find out all children (use move to find children)
            a) get the current postion for the selected node (this becomes parent node for the children)
            b) check if a valid position exist (boundary will make few nodes invalid)
            c) if any node is a wall then ignore that
            d) add to valid children node list for the selected parent

            For all the children node
                a) if child in visited list then ignore it and try next node
                b) calculate child node g, h and f values
                c) if child in yet_to_visit list then ignore it
                d) else move the child to yet_to_visit list
    """
    # find maze has got how many rows and columns
    no_rows, no_columns = np.shape(maze)

    # Loop until you find the end

    paths = []

    while len(yet_to_visit_list) > 0:

        # Every time any node is referred from yet_to_visit list, counter of limit operation incremented
        outer_iterations += 1

        # Get the current node
        current_node = yet_to_visit_list[0]
        current_index = 0
        for index, item in enumerate(yet_to_visit_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index

        # if we hit this point return the path such as it may be no solution or
        # computation cost is too high
        if outer_iterations > max_iterations:
            print("giving up on pathfinding too many iterations")
            return return_path(current_node, maze)

        # Pop current node out off yet_to_visit list, add to visited list
        yet_to_visit_list.pop(current_index)
        visited_list.append(current_node)

        # test if goal is reached or not, if yes then return the path
        if current_node == end_node:
            paths.append(return_path(current_node, maze))
            #print(paths)


        # Generate children from all adjacent squares
        children = []

        for new_position in move:

            # Get node position
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            # Make sure within range (check if within maze boundary)
            if (node_position[0] > (no_rows - 1) or
                    node_position[0] < 0 or
                    node_position[1] > (no_columns - 1) or
                    node_position[1] < 0):
                continue

            # Make sure walkable terrain
            if maze[node_position[0]][node_position[1]] != 1:
                continue

            # Create new node
            new_node = Node(current_node, node_position)

            # Append
            children.append(new_node)

        # Loop through children
        for child in children:

            # Child is on the visited list (search entire visited list)
            if len([visited_child for visited_child in visited_list if visited_child == child]) > 0:
                continue

            # Create the f, g, and h values
            child.g = current_node.g + cost
            ## Heuristic costs calculated here, this is using eucledian distance
            child.h = ((abs(child.position[0] - end_node.position[0])) +
                       (abs(child.position[1] - end_node.position[1])))

            child.f = child.g + child.h

            # Child is already in the yet_to_visit list and g cost is already lower
            if len([i for i in yet_to_visit_list if child == i and child.g > i.g]) > 0:
                continue

            # Add the child to the yet_to_visit list
            yet_to_visit_list.append(child)
    return paths

if __name__ == '__main__':

    maze = []
    size = []
    filename = input("Enter filename, please include .txt:")
    with open(filename) as f:
        first_line = f.readline()
        size.append([int(i) for i in first_line.split()])
        for line in f:
            maze.append([int(i) for i in line.split()])
    print("The matrix of size:", size)
    print("The matrix:", maze)
    # you may also want to remove whitespace characters like `\n` at the end of each line
    start = [0, 0]  # starting position
    end = [len(maze)-1, len(maze)-1]  # ending position
    cost = 1  # cost per movement

    output = search(maze, cost, start, end)
    output = output[::-1]
    output_string = '\n'.join(' '.join('%g' % x for x in y) for y in output)
    #print(path)
    #print('\n'.join([''.join(["{:" ">3d}".format(item) for item in row])
                     #for row in path]))
    text_file = open("output.txt", "w")
    text_file.write(output_string)
    text_file.close()
#The Happy Ending, thank you!