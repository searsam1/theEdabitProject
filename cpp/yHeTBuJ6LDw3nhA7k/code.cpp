#include <iostream>
#include <vector>

std::vector<std::string> makeBox(int n) {
	
	if (n == 1){
		return {"#"};
	}

	std::string middle = "#";
	for (int i=0; i<n-2; i++){
		middle += ' ';
	}
	middle += '#';

	std::string topBottom = "#";
	for (int i=0; i<n-2; i++){
		topBottom += '#';
	}
	topBottom += '#';

	std::vector<std::string> v = {topBottom};

	for (int i=1; i<n; i++){

		if (i == n-1){
			v.push_back(topBottom);
		}
		else{
			v.push_back(middle);
		}
	}
	return v;
}

int main(){
	for (std::string s : makeBox(3)){
		std::cout << "["  << s << "]"<< "\n" ;
	}
	return 0;
}






