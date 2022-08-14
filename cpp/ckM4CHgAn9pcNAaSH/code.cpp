
#include <algorithm>
#include <cctype>
#include <string>
#include <iostream>

std::string dial(std::string str) {	
	std::string data = str;
	std::transform(data.begin(), data.end(), data.begin(),
    [](unsigned char c){ return std::tolower(c); });
	std::string res;
    for (int i: data){
    	if(i >= 97 && i <= 99){res += '2';}
    	else if(i >= 100 && i <= 102){res += '3';}
    	else if(i >= 103 && i <= 105){res += '4';}
    	else if(i >= 106 && i <= 108){res += '5';}
    	else if(i >= 109 && i <= 111){res += '6';}
    	else if(i >= 112 && i <= 115){res += '7';}
    	else if(i >= 116 && i <= 118){res += '8';}
    	else if(i >= 119 && i <= 122){res += '9';}
    	else{res += char(i);}
    	}
    std::cout << res;
	return res;
}

int main() {
	dial("V");
	return 0;
}

// TestsConsoleDescribe(dial_) {

// 	It(test1){Assert::That(dial("1-800-HOTLINEBLING"), Equals("1-800-468546325464"));}

// 	It(test2){Assert::That(dial("hello-world!"), Equals("43556-96753!"));}

// 	It(test3){Assert::That(dial("aaaabcccdefggg"), Equals("22222222333444"));}

// 	It(test4){Assert::That(dial("01023468adghijgkmz?"), Equals("010234682344454569?"));}

// 	It(test5){Assert::That(dial("SwApPeDcAsE"), Equals("79277332273"));}

// 	It(test6){Assert::That(dial("VAPORWAVE"), Equals("827679283"));}

// };