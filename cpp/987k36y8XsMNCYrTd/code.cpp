#include <cmath>
int yearsInOneHouse(int age, int moves) {
	return round(float(age) / (moves + 1));
}