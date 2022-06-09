
with open("/Users/111244rfsf/Documents/Repositories/theEdabitProject/theEdabitProjectRepo/Python/tic_tac_toe/tic_tac_toe.py", "r") as f:
	file = f.read()

file = file.replace("\t", "____")
print(file)
