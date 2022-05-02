#include <iostream>
#include <vector>

std::vector<int> collatz(int n) {
	int max = n;
  	int count = 0;
  	while (n > 1)
	{
	  if (n >= max)
	  	{max = n;}
	  if (n % 2)
	  	{n = n * 3 + 1;}
	  else 
	  	{n /= 2;}
	  count++;
	}
  	return { count,max };
}

int main(int argc, char const *argv[])
{
	/* code */
	return 0;
}