#include <iostream>

int main(void)
{
/*	int* ptr;
	int x = 0;
	
	ptr = &x;
	*ptr = 47;
	
	std::cout << x << std::endl;*/

	int x = 1, y = 2;
	*x = y;

	std::cout << x << std::endl;
	std::cout << y << std::endl;	
	


	return 0;
}