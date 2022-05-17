import re 

def validate_relationships(txt):
	
	x = re.sub("<=","$",txt)
	x = re.sub(">=","@",x)
	x = re.sub("=","==",x)
	x = re.sub("\$","<=",x)
	x = re.sub("@",">=",x)
	return eval(x)



print(
	validate_relationships("-15<-10<=0=0<5")
	)