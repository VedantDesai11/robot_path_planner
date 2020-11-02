import matplotlib.pyplot as plt
import numpy as np
import cv2


class Node():
	"""A node class for A* Pathfinding"""

	def __init__(self, parent=None, position=None):
		self.parent = parent
		self.position = position

		self.g = 0
		self.h = 0
		self.f = 0

	def __eq__(self, other):
		return self.position == other.position


def astar(maze, start, end):
	# Create start and end node
	start_node = Node(None, start)
	start_node.g = start_node.h = start_node.f = 0
	end_node = Node(None, end)
	end_node.g = end_node.h = end_node.f = 0

	# Initialize both open and closed list
	open_list = []
	closed_list = []

	# Add the start node
	open_list.append(start_node)

	# Loop until you find the end
	while len(open_list) > 0:

		# Get the current node
		current_node = open_list[0]
		current_index = 0
		for index, item in enumerate(open_list):
			if item.f < current_node.f:
				current_node = item
				current_index = index

		# Pop current off open list, add to closed list
		open_list.pop(current_index)
		closed_list.append(current_node)

		# Found the goal
		if current_node == end_node:
			path = []
			current = current_node
			while current is not None:
				path.append(current.position)
				current = current.parent
			return path[::-1] # Return reversed path

		# Generate children
		children = []
		for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]: # Adjacent squares

			# Get node position
			node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

			# Make sure within range
			if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (len(maze[len(maze)-1]) -1) or node_position[1] < 0:
				continue

			# Make sure walkable terrain
			if maze[node_position[0]][node_position[1]] != 0:
				continue

			# Create new node
			new_node = Node(current_node, node_position)

			# Append
			children.append(new_node)

		# Loop through children
		for child in children:

			# Child is on the closed list
			for closed_child in closed_list:
				if child == closed_child:
					continue

			# Create the f, g, and h values
			child.g = current_node.g + 1
			child.h = ((child.position[0] - end_node.position[0]) ** 2) + ((child.position[1] - end_node.position[1]) ** 2)
			child.f = child.g + child.h

			# Child is already in the open list
			for open_node in open_list:
				if child == open_node and child.g > open_node.g:
					continue

			# Add the child to the open list
			open_list.append(child)


def main():

	world_size = [4880, 3050]

	obstacle_size = [305, 305]

	start = [305, 3050 // 2]
	goal = [305 * 15, 3050 // 2]

	obstacles = [[0.61, 2.743], [0.915, 2.743], [1.219, 2.743], [1.829, 1.219],
				 [1.829, 1.524], [1.829, 1.829], [1.829, 2.134], [2.743, 0.305],
				 [2.743, 0.61], [2.743, 0.915], [2.743, 2.743], [3.048, 2.743],
				 [3.353, 2.743]]

	obstacles = [[int(j * 1000) // 305 for j in i] for i in obstacles]

	# create maze
	maze = [[0 for i in range(3050// 305)] for j in range(4880 // 305)]

	for obstacle in obstacles:
		x, y = obstacle[0], obstacle[1]
		maze[x + 1][y + 1] = 1
		maze[x - 1][y + 1] = 1
		maze[x + 1][y - 1] = 1
		maze[x - 1][y - 1] = 1

	start = (1, 5)
	end = (14, 5)

	path = astar(maze, start, end)
	manhattan_path = []
	for i, cell in enumerate(path):
		manhattan_path.append(cell)
		if i != len(path)-1:
			next_cell = path[i+1]
			distance = abs(next_cell[0] - cell[0]) + abs(next_cell[1] - cell[1])
			if distance > 1:
				if maze[cell[0]][next_cell[1]] != 1:
					manhattan_path.append((cell[0],next_cell[1]))
				else:
					manhattan_path.append((next_cell[0], cell[1]))

	for cell in manhattan_path:
		maze[cell[0]][cell[1]] = 5

	print(manhattan_path)

	


if __name__ == '__main__':
	main()


