#include <cmath>
bool is_curzon(int n) {
	return int((1 + pow(2,n)) / (1 + 2*n)) == (1 + pow(2,n)) / (1 + 2*n);

}