
#include <iostream>
#include <vector>


/*You are given 2 out of 3 angles in a triangle, in degrees.

Write a function that classifies the missing angle as either "acute", "right", or "obtuse" based on its degrees.
*/


std::string missingAngle(int angle1, int angle2) {
	int res = abs(angle1 + angle2 - 180);
	return res < 90 ? "acute" : res == 90 ? "right" : "obtuse"; 

}


int main(int argc, char const *argv[])
{
	/* code */
	return 0;
}