#include <iostream>

std::string uncensor(std::string str, std::string vowels) 
{
	int vowelIdx = 0;
	std::string res;
	for (char chr : str)
	{
		if (chr == '*')
		{
			res += vowels[vowelIdx];
			vowelIdx += 1;
		}
		else
		{
			res += chr;
		}
	}
	return res;
}

int main()
{
	uncensor("Wh*r* d*d my v*w*ls g*?", "eeioeo");
}
