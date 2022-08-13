#include <iostream>
#include <vector>


int uploadCount(std::vector<std::string> dates, std::string month) {
	int total = 0;
	for (std::string date : dates){
	  	if (date.find(month) != std::string::npos){
	  		total ++;
	  	}
	}
	return total;
}

int main(){
	uploadCount({"Dec 10", "Dec 10", "Dec 9", "Sept 3"}, "Dec");
	return 0;
}