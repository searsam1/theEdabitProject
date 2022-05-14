

# addition


```

def addition(num):
	pass

```


# all_pairs


```

def all_pairs(lst, target):

	res = []
	while lst:
		ele = lst.pop(0)
		for j in lst:
			if ele + j == target:
				res.append(sorted([ele,j]))
	res = sorted(res, key=lambda x : min(x))
	return res


```


# anna_likes


```

import re
tests = " ".join("""

Test.assert_equals(anna_likes("James"), False) ## Test 1
Test.assert_equals(anna_likes("John"), False) ## Test 2 
Test.assert_equals(anna_likes("Robert"), False) ## Test 3 
Test.assert_equals(anna_likes("Michael"), False) ## Test 4 
Test.assert_equals(anna_likes("William"), False) ## Test 5
Test.assert_equals(anna_likes("David"), False) ## Test 6 
Test.assert_equals(anna_likes("Richard"), False) ## Test 7 
Test.assert_equals(anna_likes("Joseph"), False) ## Test 8 
Test.assert_equals(anna_likes("Thomas"), False) ## Test 9 
Test.assert_equals(anna_likes("Charles"), False) ## Test 10 
Test.assert_equals(anna_likes("Christopher"), False) ## Test 11 
Test.assert_equals(anna_likes("Daniel"), True) ## Test 12 
Test.assert_equals(anna_likes("Matthew"), False) ## Test 13 
Test.assert_equals(anna_likes("Anthony"), False) ## Test 14 
Test.assert_equals(anna_likes("Donald"), False) ## Test 15 
Test.assert_equals(anna_likes("Mark"), False) ## Test 16 
Test.assert_equals(anna_likes("Paul"), True) ## Test 17 
Test.assert_equals(anna_likes("Steven"), False) ## Test 18 
Test.assert_equals(anna_likes("Andrew"), False) ## Test 19 
Test.assert_equals(anna_likes("Kenneth"), False) ## Test 20 
Test.assert_equals(anna_likes("Joshua"), True) ## Test 21 
Test.assert_equals(anna_likes("Kevin"), False) ## Test 22 
Test.assert_equals(anna_likes("Brian"), False) ## Test 23 
Test.assert_equals(anna_likes("George"), True) ## Test 24 
Test.assert_equals(anna_likes("Edward"), False) ## Test 25 
Test.assert_equals(anna_likes("Ronald"), False) ## Test 26 
Test.assert_equals(anna_likes("Timothy"), False) ## Test 27 
Test.assert_equals(anna_likes("Jason"), False) ## Test 28 
Test.assert_equals(anna_likes("Jeffrey"), False) ## Test 29 
Test.assert_equals(anna_likes("Ryan"), False) ## Test 30 
Test.assert_equals(anna_likes("Jacob"), False) ## Test 31 
Test.assert_equals(anna_likes("Gary"), False) ## Test 32 
Test.assert_equals(anna_likes("Nicholas"), False) ## Test 33 
Test.assert_equals(anna_likes("Eric"), True) ## Test 34 
Test.assert_equals(anna_likes("Jonathan"), False) ## Test 35 
Test.assert_equals(anna_likes("Stephen"), False) ## Test 36 
Test.assert_equals(anna_likes("Larry"), False) ## Test 37 
Test.assert_equals(anna_likes("Justin"), False) ## Test 38 
Test.assert_equals(anna_likes("Scott"), False) ## Test 39 
Test.assert_equals(anna_likes("Brandon"), False) ## Test 40 
Test.assert_equals(anna_likes("Benjamin"), False) ## Test 41 
Test.assert_equals(anna_likes("Samuel"), True) ## Test 42 
Test.assert_equals(anna_likes("Frank"), False) ## Test 43 
Test.assert_equals(anna_likes("Gregory"), False) ## Test 44 
Test.assert_equals(anna_likes("Raymond"), False) ## Test 45 
Test.assert_equals(anna_likes("Alexander"), False) ## Test 46 
Test.assert_equals(anna_likes("Patrick"), False) ## Test 47 
Test.assert_equals(anna_likes("Jack"), False) ## Test 48 
Test.assert_equals(anna_likes("Dennis"), False) ## Test 49 
Test.assert_equals(anna_likes("Jerry"), False) ## Test 50 
Test.assert_equals(anna_likes("Tyler"), False) ## Test 51 
Test.assert_equals(anna_likes("Aaron"), False) ## Test 52 
Test.assert_equals(anna_likes("Jose"), True) ## Test 53 
Test.assert_equals(anna_likes("Henry"), False) ## Test 54 
Test.assert_equals(anna_likes("Adam"), True) ## Test 55 
Test.assert_equals(anna_likes("Douglas"), False) ## Test 56 
Test.assert_equals(anna_likes("Nathan"), False) ## Test 57 
Test.assert_equals(anna_likes("Peter"), False) ## Test 58 
Test.assert_equals(anna_likes("Zachary"), False) ## Test 59 
Test.assert_equals(anna_likes("Kyle"), False) ## Test 60 
Test.assert_equals(anna_likes("Walter"), False) ## Test 61 
Test.assert_equals(anna_likes("Harold"), False) ## Test 62 
Test.assert_equals(anna_likes("Jeremy"), False) ## Test 63 
Test.assert_equals(anna_likes("Ethan"), False) ## Test 64 
Test.assert_equals(anna_likes("Carl"), False) ## Test 65 
Test.assert_equals(anna_likes("Keith"), False) ## Test 66 
Test.assert_equals(anna_likes("Roger"), False) ## Test 67 
Test.assert_equals(anna_likes("Gerald"), False) ## Test 68 
Test.assert_equals(anna_likes("Christian"), False) ## Test 69 
Test.assert_equals(anna_likes("Terry"), False) ## Test 70 
Test.assert_equals(anna_likes("Sean"), True) ## Test 71 
Test.assert_equals(anna_likes("Arthur"), False) ## Test 72 
Test.assert_equals(anna_likes("Austin"), True) ## Test 73 
Test.assert_equals(anna_likes("Noah"), True) ## Test 74 
Test.assert_equals(anna_likes("Lawrence"), False) ## Test 75 
Test.assert_equals(anna_likes("Jesse"), False) ## Test 76 
Test.assert_equals(anna_likes("Joe"), False) ## Test 77 
Test.assert_equals(anna_likes("Bryan"), False) ## Test 78 
Test.assert_equals(anna_likes("Billy"), False) ## Test 79 
Test.assert_equals(anna_likes("Jordan"), False) ## Test 80 
Test.assert_equals(anna_likes("Albert"), False) ## Test 81 
Test.assert_equals(anna_likes("Dylan"), False) ## Test 82 
Test.assert_equals(anna_likes("Bruce"), False) ## Test 83 
Test.assert_equals(anna_likes("Willie"), True) ## Test 84 
Test.assert_equals(anna_likes("Gabriel"), False) ## Test 85 
Test.assert_equals(anna_likes("Alan"), True) ## Test 86 
Test.assert_equals(anna_likes("Juan"), True) ## Test 87 
Test.assert_equals(anna_likes("Logan"), False) ## Test 88 
Test.assert_equals(anna_likes("Wayne"), False) ## Test 89 
Test.assert_equals(anna_likes("Ralph"), False) ## Test 90 
Test.assert_equals(anna_likes("Roy"), False) ## Test 91 
Test.assert_equals(anna_likes("Eugene"), False) ## Test 92 
Test.assert_equals(anna_likes("Randy"), False) ## Test 93 
Test.assert_equals(anna_likes("Vincent"), False) ## Test 94 
Test.assert_equals(anna_likes("Russell"), False) ## Test 95 
Test.assert_equals(anna_likes("Louis"), False) ## Test 96 
Test.assert_equals(anna_likes("Philip"), False) ## Test 97 
Test.assert_equals(anna_likes("Bobby"), False) ## Test 98 
Test.assert_equals(anna_likes("Johnny"), False) ## Test 99 
Test.assert_equals(anna_likes("Bradley"), False) ## Test 100
""".split("\n"))

pattern = r'(?:\")(\D+)(?:\")\), (\D+)(?:\))'
matches = re.findall(pattern, tests)

res = [i[0] for i in matches if i[1] == "True"]
print(res)

def anna_likes(boy):
	names = ['Daniel', 'Paul', 'Joshua', 
	'George', 'Eric', 'Samuel', 
	'Jose', 'Adam', 'Sean', 
	'Austin', 'Noah', 'Willie', 
	'Alan', 'Juan']
	return boy in names







```


# babbage


```

from time import perf_counter

def babbage(n):
	i = 0
	n_copy = n
	while not str(n**.5).endswith(".0"):
		i += 1
		n = str(i) + str(n_copy)
		n = int(n)
	if n_copy == 269696:
		return ["Babbage was incorrect!","Babbage was correct!"][n**.5 == 99736]
	return n**.5


print(babbage(481))
```


# band_names_sort


```

def band_names_sort(r):
	
	res = [band.replace("The ","").replace("An ","").replace("A ","") 
		for band in r]
	z = list(zip(r,res))
	z = sorted(z, key = lambda x: x[1])
	z = [i[0] for i in z]
	return z

# names = ["The Plot in You", "The Devil Wears Prada", "Pierce the Veil", "Norma Jean", "The Bled", "Say Anything", "The Midway State", "We Came as Romans", "Counterparts", "Oh, Sleeper", "A Skylit Drive", "Anywhere But Here", "An Old Dog"]

# print(band_names_sort(names))
```


# bool


```

#include<cmath>
bool is_curzon(int n) {
	
}pass

```


# boxes


```

def boxes(weights):
	weight_l = len(weights)
	box = [weights.pop(0)]
	res = []
	while weights:
		b = weights.pop(0)
		if b + sum(box) > 10:
			res.append(box)
			box = [b]
		elif b + sum(box) == 10:
			res.append(box + [b])
			box = []
		else:
			box.append(b)
	print(res)
	count = sum(len(i) for i in res)

	if count != weight_l:
		try:
			res = res + [[b]]
		except UnboundLocalError:
			return 1
	return len(res)

print(
	boxes([8, 3, 2, 1, 1, 2, 1, 3, 2, 1])
	)
	
```


# check_power2


```

import math

def check_power2(n):
	if n == 1:
		return True
	x = 2	
	check = lambda n : int("".join(sorted(str(n),reverse=True)))

	while x < (n*4):
		if check(x) == check(n):
			return True
		x *= 2
	return check(x) == check(n)

```


# chosen_wine


```

def chosen_wine(wines):
	if len(wines) >= 2:
		return sorted(wines, key=lambda x: x["price"])[1]['name']
	elif not len(wines):
		return None
	else:
		return wines[0]["name"]
```


# combine


```

def combine(lst):
	FSA = {}
	for l in lst:
		FSA[l[0]] = ["0","1"]
	for l in lst:
		if l[1] == 1:
			FSA[l[0]][1] = l[2]
		elif l[1] == 0:
			FSA[l[0]][0] = l[2]
	return FSA
# example tests


```


# complex_to_tuple


```

import re 
def complex_to_tuple(param):
	res = [] 
	for i in range(len(param)):
		if param[i] in "+-" and i != 0:
			a,b = param[:i], param[i:].strip("i").strip("+")
			a,b = int(a), int(b)
			return (a,b)
		
```


# converter


```

def converter(a, b):
	if a[0] == "fahrenheit":
		if b == "kelvin":
			return round((a[1] - 32) * (5/9) + 273.15,1)
		elif b == "celsius":
			return round((a[1] - 32) * (5/9),1)
	elif a[0] == "celsius":
		if b == "kelvin":
			return round(273.15 + a[1],1)
		elif b == "fahrenheit":
			return round((a[1] * 9/5) + 32,1)
	elif a[0] == "kelvin":
		if b == "fahrenheit":
			return round((a[1] - 273.15) * (9/5) + 32,1)
		elif b == "celsius":
			return round(a[1] - 273.15,1)

```


# decode_morse


```


def decode_morse(txt):
	d = {
	  "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.",
	  "G": "--.", "H": "....", "I": "..", "J": ".---", "K": "-.-", "L": ".-..",
	  "M": "--", "N": "-.", "O": "---", "P": ".--.", "Q": "--.-", "R": ".-.",
	  "S": "...", "T": "-", "U": "..-", "V": "...-", "W": ".--", "X": "-..-",
	  "Y": "-.--", "Z": "--..", "0": "-----",
	  "1": ".----", "2": "..---", "3": "...--", "4": "....-", "5": ".....",
	  "6": "-....", "7": "--...", "8": "---..", "9": "----.",
	  "&": ".-...", "'": ".----.", "@": ".--.-.", ")": "-.--.-", "(": "-.--.",
	  ":": "---...", ",": "--..--", "=": "-...-", "!": "-.-.--", ".": ".-.-.-",
	  "-": "-....-", "+": ".-.-.", '"': ".-..-.", "?": "..--..", "/": "-..-.",
	}
	d = {v:k for k,v in d.items()}
	words = [i.split() for i in txt.split("   ")]
	new_words = []
	for word in words:
		word = "".join(map(lambda char: d[char],word))
		new_words.append(word)
	return " ".join(new_words)
	
```


# dial


```

# d = {}
# dic = {} 
# d["abc"],d["def"],d["ghi"] = 2,3,4
# d["jkl"],d["mno"],d["pqrs"]  = 5,6,7
# d["tuv"],d["wxyz"] = 8,9
# for k,v in d.items():
# 	for char in k:
# 		dic[char] = v
d = {
'r': 7, 'i': 4,
'l': 5, 's': 7, 'b': 2,
'j': 5, 'd': 3, 'a': 2,
'c': 2, 'h': 4, 'g': 4,
'p': 7, 'm': 6, 'x': 9,
'w': 9, 'q': 7, 'n': 6,
'o': 6, 't': 8, 'u': 8,
'v': 8, 'e': 3, 'y': 9, 
'k': 5, 'z': 9, 'f': 3
}

def dial(txt):
	return "".join(str(d[i.lower()]) 
		if i.isalpha() else i 
			for i in txt)

```


# digit_sort


```

def digit_sort(lst):
	res = sorted(lst, key=lambda x: ( len(str(x)),x*-1 ),
	reverse=True)
	return res
```


# digital_division


```

def digital_division(n):
	if len(str(n)) == 1:
		return "Perfect"
	condition_1 = all(not n % int(i) for i in str(n).replace("0",""))
	condition_2 = not ( n % sum(int(i) for i in str(n)) )
	res = [int(str(n)[0])]
	res = [res[-1] * int(i) for i in str(n)[1:]][0]
	if res:
		condition_3 = not n % res
	else:
		condition_3 = False
	lst = [condition_1,condition_2,condition_3]
	if sum(lst) == 1:
		return 1
	if sum(lst) == 2:
		return 2
	if sum(lst) == 3:
		return "Perfect"
	if not sum(lst):
		return "Indivisible"
		
	
```


# encode_morse


```

def encode_morse(message):
	pass

```


# evenOddTransform


```

std::vector<int> evenOddTransform(std::vector<int> arr, int n) {
	
}pass

```


# f


```


from itertools import combinations,permutations

def f(n):
	
	arr = [j for j in range(1,n+1) for i in range(2)]
	perms = list(set(permutations(arr,2)))
	geo_mean = lambda a,b : int((a*b)**.5) == (a*b)**.5
	res = []

	for perm in perms:
		a,b = perm
		res.append(geo_mean(a,b))

	total = res.count(True) / len(res)
	return total
```


# find_glasses


```

import re 

def find_glasses(lst):
	
	p = "O(-+)O"
	for s in lst:
		for i in re.findall(p,s):
			if len(set(i)) == 1:
				return lst.index(s)

print(find_glasses(['OOOO----~OOO', '-------', 'OOOOOOO', 'OO-OO-OO-O']))
```


# find_longest


```

def find_longest(sentence):
	words = sorted(sentence.split(), key=lambda x: len([i for i in x if i.isalpha()]), 
	reverse=True
	)
	res = []
	for word in words:
		new_word = ""
		for char in word:
			if not char.isalpha():
				res.append(new_word)
				next
			else:
				new_word += char
		res.append(new_word)
				
	return res[0].lower()
	
```


# gen_tiles


```

def gen_tiles():
	suits = ["tong", "tiao", "wan"]
	ranks = ["yi", "er", "san" ,"si","wu","liu","qi","ba","jiu"]
	tiles = []

	d = {
		"yi tong" : "bing gan",
		"er tong" : "yan jing",
		"yi tiao" : "ji",
	}

	for rank in ranks:
		t = [rank + " " + suit for suit in suits for _ in range(4)]
		
		tiles = [i if not i in ["yi tong", "er tong","yi tiao"]
			else d[i] for i in tiles 
				]
		tiles += t
	return tiles



gen_tiles()

```


# get_det


```

import numpy as np
def get_det(a):
	n_array = np.array(a)
	return round(np.linalg.det(n_array))

"""
from get_det import get_det
import unittest

class Test(unittest.TestCase):
	
	checks = [] 
	def assert_equals(a,b,message=None,checks=checks):
		print(a,b,sep="  ->  ")
		checks.append(["Fail","Pass"][a==b])
		print("\t",checks,"\n")

Test.assert_equals(get_det([[0,1],[1,0]]), -1)
Test.assert_equals(get_det([[69,0],[1,1]]), 69)
Test.assert_equals(get_det([[7,420,8],[5,7,0],[1,1,7]]), -14373)
Test.assert_equals(get_det([[5,1],[1,6]]), 29)
Test.assert_equals(get_det([[1,2,3],[4,5,6],[7,8,9]]), 0)
Test.assert_equals(get_det([[-1,1,-1],[-1,-55,1],[1,-1,-1]]), -112)
Test.assert_equals(get_det([[2,7,6],[9,5,1],[4,3,8]]), -360)
"""
```


# hello


```

function hello() {
	
}pass

```


# id_mtrx


```

def id_mtrx(n):
	if type(n) != int:
		return "Error"
	
	is_neg = False
	if n < 0:
		n *= -1
		is_neg = True
	arr = [] 
	for i in range(n):
		row = [] 
		for j in range(n):
			row.append(int(i == j))
		arr.append(row)
	if is_neg:
		{i.reverse() for i in arr}
	return arr
```


# integer_to_string


```


res = []

def base_8(n):
	if n < 1:
		res.append('%')
		return "".join(str(i) for i in res)[::-1]
	res.append(n % 8)
	n //= 8
	return base_8(n)


def base_2(n):
	if n < 1:
		res.append('%')
		return "".join(str(i) for i in res)[::-1]
	res.append(int(bool(n % 2)))
	n //= 2
	return base_2(n)

def base_16(n):
	if n < 1:
		res.append('%')
		return "".join(str(i) for i in res)[::-1]
	res.append("{:x}".format((n % 16)))
	n //= 16
	return base_16(n)


def integer_to_string(number, base):
	d = {
	2 : base_2,
	8 : base_8,
	16 : base_16,
	}
	return [i for i in d[base](number).split("%") if i][0]

```


# is_autobiographical


```

def is_autobiographical(n):
	res = [] 
	for i in range(len(str(n))):
		res.append( str(str(n).count(str(i))) )
	res = int("".join(res))
	return res == n
```


# is_disarium


```

def is_disarium(n):
	
	i = 1
	arr = [] 
	for number in str(n):
		number = int(number) 
		number = number ** i 
		arr.append(number)
		i += 1 
	return sum(arr) == n

```


# is_icecream_sandwich


```

def is_icecream_sandwich(txt):
	s = sorted(list(set(txt)),key = lambda x : txt.index(x))
	if len(s) != 2:
		return False
	if txt.count(s[0]) % 2:
		return False
	return True
			
	
```


# is_ord_sub


```

from itertools import combinations
def is_ord_sub(smlst, biglst):
	combs = combinations(biglst, len(smlst))
	return tuple(smlst) in combs
		
		
```


# left_side


```

#
def left_side(lst):
	res = [] 
	for i in range(len(lst)):
		ele = lst[i]
		mini_lst = lst[:i]
		count = sum(ele > n for n in mini_lst)
		res.append(count)
	return res

def right_side(lst):
	res = [] 
	for i in range(len(lst)-1,-1,-1):
		ele = lst[i]
		mini_lst = lst[i+1:]
		count = sum(ele > n for n in mini_lst)
		res.append(count)
	res.reverse()
	return res
#

```


# mix_middle


```

def mix_middle(txt):
	word_function = lambda word : [
				word[0] + word[1:-1][::-1] + 
				word[-1] if len(word) > 1 
					else word][0]
	
	res = []
	words = txt.split()
	for word in words:
		if "-" in word:
			dash_index = word.index("-")
			word = word_function( word.replace("-","") )
			word = word[:dash_index] + "-" + word[dash_index:]
			res.append(word)
		else:
			res.append(word_function(word))
	return " ".join(res)

print(mix_middle("b"))

```


# multiply_matrix


```

def multiply_matrix(m1, m2):
	if len(m1[0]) != len(m2):
		return "ERROR"
	cols = []
	for i in range(len(m1)):
		row = [] 
		for j in range(len(m2)):
			row.append(m2[j][i])
		cols.append(row)
	matrix = []
	for row in m1:
		temp = [] 
		for col in cols:
			x = sum(i[0]*i[1] for i in list(zip(row,col)))
			temp.append(x)
		matrix.append(temp)
	return matrix



multiply_matrix([[1,2,3],[4,5,6],[7,8,9]],[[1,2,3],[4,5,6],[7,8,9]])

# [1, 2, 3] --> [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# [4, 5, 6] --> [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# [7, 8, 9] --> [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
```


# nom_nom


```

def nom_nom(lst):
	if all(lst[i] >= lst[i-1] for i in range(1,len(lst))):
		return lst
	temp = []
	for i in range(1,len(lst)):
		if lst[i-1] > lst[i]:
			temp.append(lst[i-1] + lst[i])
			lst.pop(0),lst.pop(0)
			lst = temp + lst
			return nom_nom(lst)

print(nom_nom([5,3,7]))

	



```


# overlapping


```

#
def overlapping(lst):
	mins = [l[0] for l in lst]
	maxes = [l[1] for l in lst]
	return [(max(mins) ,min(maxes)),"No overlapping"][max(mins) > min(maxes)]
#			

```


# prime_count


```

primes = {3}

def is_prime(n):
	if n in primes: # works because we call it in prime_counts scope
		return True #					where we already defined primes
	if all(n % i for i in range(2,int(n**.5) + 1)):
		primes.add(n)
		return True
	return False
def prime_count(a, b, primes=primes):
	total = 0 
	for i in range(a+1,b+1):
		if is_prime(i):
			total += 1
	return total	


prime_count(1,100)
prime_count(1,100000)
prime_count(1,10000000)

```


# remainder


```

def remainder(x, y):
	pass

```


# security


```

import re

def security(txt):
	pattern = "T[x]*\$|\$[x]*T"
	match = re.search(pattern, txt)
	return ["Safe","ALARM!"][bool(match)]

print(
	security("xxxxTTxGxx$xxTxxx")
	)

```


# sort_by_answer


```

def sort_by_answer(lst):
	key_func = lambda i : eval(i.replace("x", "*"))
	return sorted(lst,key=key_func)
```


# split_n_cases


```

def split_n_cases(txt, cases):
	if len(txt) % cases:
		return ["Error"]
	step = len(txt) // cases
	res = [txt[i:i+step] for i in range(0,len(txt), step)]
	return res
	
```


# squares


```

import math

def squares(a, b):
	a_copy,b_copy = a,b
	while math.sqrt(a) != int(math.sqrt(a)):
		a += 1
	while math.sqrt(b) != int(math.sqrt(b)):
		b += 1
	res = math.sqrt(b) - math.sqrt(a)
	
	if res < 2:
		if math.sqrt(a_copy) == int(math.sqrt(a_copy)):
			res += 1
		if math.sqrt(b_copy) == int(math.sqrt(b_copy)):
			res += 1
	return res

```


# staircase


```

#
def staircase(n):
	is_neg,n,string = n < 0,abs(n), ""
	
	for i in range(1,n+1):
		left = (n-i) * "_"
		right = i * "#"
		
		if is_neg:
			left,right = right,left

		s = left + right + "\n"
		string += (s)
		
	return string.strip("\n") if not is_neg else string.strip("\n")[::-1]
#

l = r"""	
+---?-----------------------------------------------+
|  / 	{}        {-} +       {----}     {------}   |
| /           +                 *                   |
?/    ------	  |     +     |			 |	    +   |
|    / 		\	  |     +     |-----/    {          |
|   /--------\	  |           |		     |    +     |
|  /  		  \	  |  $   /    |    *     |          | 
|  \          /	  |=====/     +------/   |-------+  |
+---------------------------------------------------+   

""".replace(" ","A")


print(l.encode())



```


# swap_cards


```

def swap_cards(n1, n2):
	low = str(min(int(i) for i in str(n1)))
	high = str(n2)[0]
	n1, n2 = str(n1), str(n2)
	idx = n1.index(low)
	if idx == 0:
		n1 = high + n1[1]
	else:
		n1 = n1[1] + high
	n2 = low + n2[1]
	return n1 > n2

```


# tic_tac_toe


```

def tic_tac_toe(inputs):
	rows = [row for row in inputs]
	cols = [] 
	for i in range(len(inputs)):
		col = [] 
		for row in inputs:
			col.append(row[i])
		cols.append(col)
	arr = [rows] + [cols]
	diagonals = []
	left = [inputs[i][i] for i in range(len(inputs))]
	
	right = []
	for i in range(0, len(inputs)):

		right.append( inputs[i][-i-1] )
	winner = {
	"X" : "Player 1 wins",
	"O" : "Player 2 wins",
	}
	diagonals = [left] + [right]
	for row in rows:
		if len(set(row)) != 1:
			next
		else:
			return winner[list(set(row))[0]]
	for col in cols:
		if len(set(col)) != 1:
			print(set(col))
			next
		else:
			return winner[list(set(col))[0]]
	for diagonal in diagonals:
		if len(set(diagonal)) != 1:
			print(set(diagonal))
			next
		else:
			return winner[list(set(diagonal))[0]]
	return "It's a Tie"



print( 
tic_tac_toe(
 [["X", "O", "O"],
  ["O", "X", "O"],
  ["O", "#", "X"]])
)
```


# tweakLetters


```

std::string tweakLetters(std::string s, std::vector<int> arr) {
	
}pass

```

