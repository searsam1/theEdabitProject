function operation(num1, num2) {
	return num1 + num2 == 24 ? 
	  "added" : num1 - num2 == 24 ? 
	  	"subtracted" : num1 * num2 == 24 ?
	  "multiplied" : num1 / num2 == 24 ?
	  "divided" : null;  
}