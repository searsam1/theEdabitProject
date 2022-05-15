#include <vector>
#include <iostream>

std::vector<int> sumOddAndEven(std::vector<int> arr) {
	int odd_sum = 0;
	int even_sum = 0;
	for (int i : arr){
		if (i % 2){
			odd_sum += i;
		}
		else {
			even_sum += i;
		}
	}
	return { even_sum,odd_sum };
}

int main(void)
{
	;
}