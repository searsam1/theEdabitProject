import random

def exit_maze(maze, directions):
	
	start_cordinates = [(i,row.index(2)) for i,row in enumerate(maze) if 2 in row][0]
	check_value = lambda y,x:  maze[y][x]

	y,x = start_cordinates
	north, south = lambda y,x : (y-1, x+0), lambda y,x : (y+1, x+0)
	east, west = lambda y,x : (y+0, x+1), lambda y,x : (y+0, x-1)
	try_direction = lambda direction : {
		"N" : north, 
		"S" : south, 
		"E" : east, 
		"W" : west
		}[direction]

	for direction in directions:
		try:
			y,x = try_direction(direction)(y,x)
			if check_value(y,x) == 1:
				return "Dead"
			if check_value(y,x) == 3:
				return "Finish"
		except IndexError as e:
			return "Dead"
	return ["Lost","Finish"][check_value(y,x) == 3]


def gen_maze(size):
	y,x = size
	zero_or_one = lambda : random.randint(0,1)
	maze = [[zero_or_one() for i in range(x)] for i in range(y)]
	
	random_start = [random.randint(0,y-1), random.randint(0,x-1)]
	random_end = [random.randint(0,y-1), random.randint(0,x-1)]
	
	y_start, x_start = random_start
	y_end, x_end = random_end
	
	maze[y_start][x_start] = 2
	maze[y_end][x_end] = 3
	
	return maze


maze = gen_maze((20,20))
for i in maze:
	print(i)
print( exit_maze(maze, input("Direction (N S E W): ").upper().split()) )
