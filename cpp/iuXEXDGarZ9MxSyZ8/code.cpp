#include <iostream>
#include <algorithm>    // std::sort
#include <vector>       // std::vector
float median(std::vector<int> arr) {
	int m = 0;
	std::sort(arr.begin(), arr.end());
	if (arr.size() % 2 != 0){
		m = arr.size() / 2;
		return arr[m];
	}
	else{
		m = arr.size() / 2;
		return (arr[m] + arr[m - 1]) / 2.0;
	}	
}

int main(){
	median({1,2,2,22,2,3,4,5});
	return 0;
}

// # Mina Yossry
// float median(std::vector<int> arr) {
// 	std::sort(arr.begin(), arr.end());
// 	if (arr.size()%2 != 0)
// 		return arr.at(arr.size()/2);
// 	else
// 		return (arr.at(arr.size()/2) + arr.at(arr.size()/2-1)) / 2.0; 
// }