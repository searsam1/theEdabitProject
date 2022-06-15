#include <iostream>
#include <vector>

// 'X' = ascii 88
std::string whoWon(std::vector<std::vector<char>> board) {
	int winner = 0;
	for (std::vector<char> row : board){
		for (int n : row){
			if (n == 88){
				winner += 88;
			}
		}
	}
	return winner == 440 ? "X" : winner == 352 ? "Tie" : "O";
}


int main(int argc, char const *argv[])
{
	std::cout <<  whoWon({
			{'X', 'O', 'X'},
			{'X', 'O', 'O'},
			{'X', 'X', 'O'}
	}) << "\n";
	
}