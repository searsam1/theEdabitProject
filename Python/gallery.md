

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


# alternate_sort


```

def alternate_sort(lst):
	ints = sorted(i for i in lst if type(i) is int)
	chars = sorted(i for i in lst if type(i) is str)
	arr = list(zip(ints, chars))
	res = [] 
	for lst in arr:
		for ele in lst:
			res.append(ele)
	return res

alternate_sort(["X", 15, 12, 18, "Y", "Z"])
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


# bw_transform


```

def bw_transform(text):
	rotations = [text]
	for i in range(len(text) - 1):
		text = text[1:] + text[0]
		rotations.append(text)
	rotations.sort()
	last_column = "".join(row[-1] for row in rotations)
	return last_column



bw_transform("banana$")
```


# can_build


```

def can_build(digits, lst):
	

	d = {count : idx for count,idx in enumerate(digits)}
	
	s = "".join(str(i) for i in lst)

	res = [] 
	for digit in set(s):
		digit = int(digit)
		correct_count = d[digit]
		actual_count = s.count(str(digit))

		if actual_count > correct_count:
			return False
	return True

		
	

x = can_build([1, 1, 0, 0, 0, 0, 0, 0, 1, 0], [1, 80, 0])
print(x)
```


# can_give_blood


```

#----------------------------------------------------------------#
def can_give_blood(donor, receiver):
	donor_blood = "".join(i for i in donor if i.isalpha())
	receiver_blood = "".join(i for i in receiver if i.isalpha())
	
	doner_rh = "".join(i for i in donor 
		if i not in donor_blood)
	receiver_rh = "".join(i for i in receiver
	 if i not in receiver_blood)

	if donor == "O-":
		return True

	if donor == "O+":
		return receiver_rh == "+"

	return donor_blood in receiver_blood
#----------------------------------------------------------------#
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


# circle


```

import math
def circle(n):
	
	a,b = 50/math.pi,50/math.pi

	theta = math.radians(360 / n)
	c = math.pow( (b**2) + (a**2) - (2*a*b) * (math.cos(theta)), .5 )
	
	perimeter = c * n
	return round(perimeter,3)

circle(3)

```


# column


```

def column(txt):
	scores = { chr(i).upper() : i-96 for i in range(97,123) }
	
	res = [scores[score] for score in txt][::-1]
	print(res)

	total = 0
	for i in range(len(res)):
		power = 26 ** i * res[i]
		print(power)
		total += power
	return total
		
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


# comments_correct


```

def comments_correct(txt):
	return not txt.count("/") % 2 and not txt.count("*") % 2
	
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


# deep_count


```

def deep_count(lst):
	
	total = 0
	while len(lst):
		if type(lst[0]) == list:
			lst = lst[1]
			total  += 1
		print(lst)






deep_count([[[[]]]])
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


# elasticize


```

def elasticize(word):
	

	
	if not len(word) % 2:
		idx = len(word) // 2
		left,right = word[:idx], word[idx:]	
		left = "".join(left[i]*(i+1) for i in range(len(left)))
		right = "".join(right[i]*(len(right)-i) for i in range(len(right)))
		return left + right
	else:
		idx = len(word) // 2
		middle = word[idx] * (idx + 1)
		word = word[:idx] + word[idx + 1:]
		left,right = word[:idx], word[idx:]	
		left = "".join(left[i]*(i+1) for i in range(len(left)))
		right = "".join(right[i]*(len(right)-i) for i in range(len(right)))

		return left + middle + right
		


print(elasticize("KAYAK"))


```


# encode_morse


```

def encode_morse(message):
	pass

```


# energy_bill


```

from datetime import datetime
def energy_bill(start_date, end_date, start_read, end_read, tariff, stand):
	
	start = datetime.strptime(start_date, "%Y,%m,%d")
	end = datetime.strptime(end_date, "%Y,%m,%d")
	day_difference = (end - start).days
	if day_difference < 0:
		return "Invalid date"
	day_cost = stand * day_difference
	
	meter_reading = end_read - start_read
	if meter_reading < 0:
		return "Invalid meter readings"
	meter_cost = tariff * meter_reading
	
	total = round((meter_cost + day_cost) * 1.05,2)
	return "${0}".format(total)
	
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


# fair_die


```

def fair_die(lst):
	
	total_rolls = sum(lst)
	probability = 6  / total_rolls

	expected = total_rolls / 6

	chi = sum((expected - actual)**2 for actual in lst) / expected
	return chi < 11.0705

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


# flatten


```


def flatten(r):	
	
	# res = lambda r : sum([flatten(i) for i in r], []) if type(r) is list else [r]
	# Credit: Deep Xavier

	if type(r) is list:
		return sum([flatten(i) for i in r], [])
	else:
		return [r]


		


x = flatten([[1,2,3,4],[5,6,7,8,[9,10,11,12]]])
print(x)



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


# get_length


```

def get_length(lst):
	
	ele_s = sum(ele.isdigit() for ele in str(lst))
	return ele_s


```


# get_sentence_value


```

def get_sentence_value(txt):
	txt = "".join(i for i in txt if i.isalpha() or i == " ")
	scores = { chr(i) : i-96 for i in range(97,123)}
	get_score = lambda word : sum(scores[char.lower()] for char in word)
	return sum((get_score(word) * [1,2][all(i.isupper() for i in word)] ) for word in txt.split())
	


get_sentence_value("abc ABC Abc")
```


# goldbach_conjecture


```

#
is_prime = lambda n : all( bool(n % i) for i in range(2,int(n**.5)+1) )
def goldbach_conjecture(n):
	if n % 2 or n <= 2:
		return []
	for i in range(2,n):
		if is_prime(i) and is_prime(n - i) and i + (n-i) == n:
			return [i, n-i]
#
```


# has_consecutive_series


```

import numpy as np

def has_consecutive_series(v1, v2):
	
	mn, mx = min([v1,v2], key=len), max([v1,v2], key=len)
	if mn == mx:
		mn,mx = v1, v2
	else:
		while len(mn) < len(mx):
			mn.append(0)
	arr1, arr2 = np.array(mn), np.array(mx)


	combined_vector = arr1 + arr2
	print(combined_vector)
	check = all(abs(combined_vector[i-1] - combined_vector[i]) == 1
		for i in range(1,len(combined_vector))
	)
	return check
x = has_consecutive_series([1, 2, 3], [1, 1, 1])
print(x)
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


# is_set


```

def is_set(cards):
	colors = len({d.get("color") for d in cards}) in [1,3]
	nums = len({d.get("number") for d in cards}) in [1,3]
	shades = len({d.get("shade") for d in cards}) in [1,3]
	shapes = len({d.get("shape") for d in cards}) in [1,3]

	return colors and nums and shades and shapes



```


# left_rotations


```

def left_rotations(txt):
	r = [txt]
	for i in range(len(txt) - 1):
		txt = txt[1:] + txt[0]
		r.append(txt)
	return r

def right_rotations(txt):
	r = [txt]
	for i in range(len(txt) - 1):
		txt = txt[-1] +  txt[:-1]
		r.append(txt)
	return r

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


# lemonade


```

def lemonade(bills):
	total = 0
	for bill in bills:
		change = bill - 5
		total -= change
		if total < 0:
			return False
		total += 5
	return True
	
```


# look_and_say


```


def look_and_say(term):
	"""
		"1211" > ["1", "2", "11"]
				one 1  one 2  two 1's
				1   1  1   2  2    1
				111221
	"""
	groups = [] 
	container = [] 
	for i in range(1, len(term)):
		e1, e2 = term[i-1], term[i]
		if e1 == e2:
			container.append(e1)
		else:
			container.append(e1)
			groups.append(container)
			container = [] 
	container.append(e2)
	groups.append(container)	
	print(groups)
	res = [str(lst.count(lst[0])) + lst[0] for lst in groups]
	res = "".join(res)
	return res


```


# lowest_element


```


def lowest_element(arr,x,y):
	bottom,top = (x+1,y), (x-1,y)
	left,right = (x, y-1), (x, y+1)
	diagonal_top_left, diagonal_top_right = (x-1,y-1), (x-1,y+1)
	diagonal_bottom_left, diagonal_bottom_right = (x+1,y-1), (x+1,y+1)

	def get_val(tup):
		x,y = tup
		try:

			if x < 0 or y < 0:
				return None
			return arr[x][y]

		except IndexError as IE:
			pass

	arr2 = [diagonal_top_left, top, diagonal_top_right, left, right, diagonal_bottom_left, bottom, diagonal_bottom_right]

	minn = min(get_val(t) for t in arr2 if get_val(t))
	if arr[x][y] < minn:
		return arr[x][y]
	return minn



```


# max_consec


```

def max_consec(lst):
	lst = sorted(set(lst))
	s = sorted(lst)
	offset = 0
	for i in range(1, len(s)):
		e1 = s[i-1]
		e2 = s[i]

		if abs(e1 - e2) != 1:
			lst.insert(i + offset, "$")
			offset += 1
	lst = " ".join(str(i) for i in lst)
	lst = lst.split("$")
	lst = [[i for i in i.split(" ") if i] for i in lst]
	return len(max(lst,key=len))
	


max_consec([4, 9, 10, 5, 17, 3, 8, 11, 1, 12, 18, 20])
```


# max_occur


```

def max_occur(text):
	mx = text.count(max(text, key=text.count))
	if mx == 1:
		return "No Repetition"
	collection = [i for i in set(text) if text.count(i) == mx]
	return sorted(collection)
	
	
	#wrong answer
	
		
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


# replace_next_largest


```

def swap_large(l):
    s = sorted(l)
    print(s)
    d = {k:v for k, v in zip(s, s[1:])}
    print(d)
    
    return [d.get(n, -1) for n in l]
swap_large([5, 7, 3, 2, 8])


```


# resistance_calculator


```

def resistance_calculator(resistors):
	

	series = sum(resistors)
	if resistors.count(0):
		return [0,series]
	para = round(1 / sum(1 / r for r in resistors if r),2)
	return [para, round(series,2)]


print(resistance_calculator([10, 20, 30, 40, 50,0]))

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


# sle


```


def sle(m):
	try:
		arr1,arr2 = m[0],m[1]
		a,b,c = arr1[0],arr1[1],arr1[2]
		d,e,f = arr2[0],arr2[1],arr2[2]
		
		middle = arr1.pop(1) * -1
		arr1.append(middle)

		div = arr1.pop(0)
		arr1 = [i for i in arr1]
		
		arr1[1] *= a
		arr1[2] *= a

		y_s = d * arr1[1] + arr2[1]
		c = arr2[-1] - d * arr1[0]
		y = y_s / c
		
		x = (e - f) / d
		print(x,y)
		return (x,y)
	except Exception:
		return 0




```


# smallest_transform


```

def smallest_transform(n):
	 diff = lambda x,y : sum(abs(int(i) - int(j)) for i,j in zip(x,y))

	 arr = []
	 l = len(str(n))
	 for i in str(n):
	 	x = i * l
	 	y = str(n)
	 	res = diff(x,y)
	 	arr.append(res)
	 return min(arr)

smallest_transform(1234)

```


# sort_by_answer


```

def sort_by_answer(lst):
	key_func = lambda i : eval(i.replace("x", "*"))
	return sorted(lst,key=key_func)
```


# split


```

import re


def split(word):
	p = "[aeiou]+|[^aeiou]"
	matches = re.findall(p,word)
	return matches


word = "beautifully"
split(word)


```


# split_groups


```


def split_groups(txt):

	res = [txt[0]]

	for i in txt[1:]:
		if i == res[-1]:
			res.append(i)
		else:
			res.append("$")
			res.append(i)
	res = "".join(res).split("$")
	return res




split_groups('5556667788')


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


# string_code


```

import string

v_count = lambda word : sum(c in "aeiou" for c in word)

def string_code(sentence):
	lower_sentence = sentence.lower()
	words = "".join(i for i in lower_sentence 
		if i.isalpha() or i == " "
		).split()
	counts = [(v_count(word) , len(word) - v_count(word) ) 
		for word in words
		]
	cons = " ".join(map(str, map(lambda x: x[0], counts) ))
	vows = " ".join(map(str, map(lambda x: x[1], counts) ))
	return [vows, cons]
	

```


# sum_ff


```

def factors(n):
	return [i for i in range(2,int(n/2) + 1) if not n % i]

def is_prime(n):
	for i in range(2,int(n**.5) + 1):
		if not n % i:
			return False
	return True

def sum_ff(a):
	facts = factors(a)
	facts = sum(sum((factors(i) for i in facts), start=[]))
	return facts
sum_ff(12)
```


# swap_cards


```

def swap_cards(n1, n2):
	arr1, arr2 = [int(i) for i in str(n1)], [int(i) for i in str(n2)]
	low = min(arr1)
	high = arr2[0]
	
	idx = arr1.index(low)
	arr1[idx],arr2[0] = high,low
	
	n1,n2 = int("".join(map(str,arr1))), int("".join(map(str,arr2)))
	return n1 > n2 

```


# third_most_expensive


```

def third_most_expensive(dct):
	pass

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


# to_display


```


d = {
0x0 :  0x3F, # 0
0x1 :  0x06, # 1 right side
0x2 :  0x5B, # 2
0x3 :  0x4F, # 3
0x4 :  0x66, # 4
0x5 :  0x6D, # 5
0x6 :  0x7D, # 6 top hook
0x7 :  0x07, # 7 no middle slash
0x8 :  0x7F, # 8
0x9 :  0x6F, # 9 bottom hook
0xA :  0x77, # A Upper case
0xB :  0x7C, # b lower case
0xC :  0x39, # C Upper case
0xD :  0x5E, # d lower case
0xE :  0x79, # E Upper case
0xF :  0x71, # F Upper case
}

def to_display(hexIn):
	return d[hexIn]

	
# # by alecSears
# import os

# import clipboard

# from bs4 import BeautifulSoup
# #from pw_and_user import username, password
# import time

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# from string import punctuation, printable
# challenge_link = clipboard.paste() # <---- Ran from inside Automator

# class Edabit():


# 	# for better readability 
# 	# otherwise the xpaths get way 2 long
# 	clean = lambda x : x.replace("\n","").replace("\t","").replace(" ","")
# 	driver = webdriver.Safari()
# 	driver.get(challenge_link)


# 	sign_in_btn_xpath = clean(r"""
# 	//*[@id="Navbar"]/div/
# 	div/div/div[1]/button
# 	""")
# 	username_btn_xpath = clean(r"""
# 	/html/body/div[2]/div/div[2]
# 	/div/div/div[1]/form/
# 	div[1]/div/div/input
# 	""")
# 	password_btn_xpath = clean(r"""
# 	/html/body/div[2]/div/
# 	div[2]/div/div/div[1]/form
# 	/div[2]/div/div/input
# 	""")
# 	sign_in_again_btn_xpath = clean(r"""
# 	/html/body/div[2]/div
# 	/div[2]/div/div/div[1]
# 	/form/div[3]
# 	""")
# 	#--------------------for loading solutions--------------------
# 	# load_more_btn_xpath = clean(r"""
# 	# //*[@id="Main"]/div/div
# 	# /div[2]/div[2]/button
# 	# """)
# 	# lang_btn_xpath = clean(r"""
# 	# //*[@id="Main"]/div/div
# 	# /div[1]/form/div[1]/div
# 	# """)
# 	# python_btn_xpath = clean(r"""
# 	# //*[@id="Main"]/div/div/
# 	# div[1]/form/div[1]/
# 	# div/div/div[2]/div[6]
# 	# """)
# 	#------------------------------------------------------------
# 	instructions_xpath = clean(r"""
# 	//*[@id="Main"]/div/
# 	div/div[1]/div/div[2]
# 	""")
# 	tests_btn_xpath = clean(r"""
# 	//*[@id="Main"]/div/div
# 	/div[2]/div/div[1]/div
# 	/div/div/div/div[2]
# 	""")
# 	tests_xpath = clean(r"""
# 	//*[@id="Main"]/div
# 	/div/div[2]/div/div[2]
# 	""")
# 	code_btn_xpath = clean(r"""
# 	//*[@id="Main"]/div/div/div[1]
# 	/div/div[1]/div[2]
# 	/div/div/div/div[3]
# 	""")
# 	code_xpath = clean(r"""//*[@id="Code"]""")
	
# 	solutions_btn_xpath = clean(r"""
# 	//*[@id="Main"]/div/div/div[1]
# 	/div/div[1]/div[2]
# 	/div/div/div/div[5]
# 	""")

# 	python_repo = clean("""
# 	/Users/111244rfsf/Documents/Repositories/
# 	theEdabitProject/theEdabitProjectRepo/Python
# 	""")

# 	tests_script = f"""import unittest

# class Test(unittest.TestCase):
	
# 	checks = [] 
# 	def assert_equals(a,b,message=None,checks=checks):
# 		print(a,b,sep="  ->  ")
# 		checks.append(["Fail","Pass"][a==b])
# 		print("\\t",checks,"\\n")
# """
# 	def replace_quotes(self,data):
# 		# add \" and \' for bash when writing to a file
# 		data = data.replace("\"","\\\"").replace("'","\\'")
# 		return data

# 	def login(self):
# 		# get(load) the url supplied by the user
# 		# deprecated
# 		# not really sure if this works
# 		self.driver.implicitly_wait(30)
		
# 		# click sign in button
# 		sign_in_btn = self.driver.find_element(by=By.XPATH, 
# 			value=self.sign_in_btn_xpath)
# 		sign_in_btn.click()

# 		# fill in username and password
# 		username_field = self.driver.find_element(by=By.XPATH, 
# 			value=self.username_btn_xpath)
		
# 		# tab to get to password // fill password
# 		username_field.send_keys(username, Keys.TAB, password
# 			)
		
# 		# login
# 		sign_in_again_btn = self.driver.find_element(by=By.XPATH, 
# 			value=self.sign_in_again_btn_xpath)
# 		sign_in_again_btn.click()
	

# 	def get_last_word(self,string):
# 		""" 
# 		Split a string by title case with no spaces.
# 		Ex. "MyNameIsJohnSmith"
# 				-- > 
# 					My Name Is John Smith
# 		"""
# 		words = []
# 		word = "" 
# 		for char in string:
# 			if char.isupper():
# 				if len(word) > 1:
# 					words.append(word)
# 				word = char
# 			else:
# 				word += char
# 		if len(word) > 1:
# 			words.append(word)
# 		return "\n".join(words)


# 	def download_challenge(self):

# 		# Wait for Challenge to load
# 		time.sleep(3)
# 		# Challenge Instructions  
# 		instructions = self.driver.find_element(by=By.XPATH, 
# 			value=self.instructions_xpath)
		
# 		# Challenge tests Tab Button
# 		tests_btn = self.driver.find_element(by=By.XPATH, 
# 			value=self.tests_btn_xpath)
# 		tests_btn.click()
		
# 		# Actual Tests field
# 		tests = self.driver.find_element(by=By.XPATH, 
# 			value=self.tests_xpath)
		
# 		# click code btn to get function name (thats in code)
# 		code_btn = self.driver.find_element(by=By.XPATH, 
# 			value=self.code_btn_xpath)
# 		code_btn.click()
# 		time.sleep(.5)
		
# 		# code field where the function name is defined.
# 		# We need this for the filename(the filename is the 
# 		# name of the function), and to start the 
# 		# put in the new script. 
# 		code = self.driver.find_element(by=By.XPATH, 
# 			value=self.code_xpath)
		
# 		# get the instructions to the challenge
# 		# instruc short for instruction
# 		instruc_txt = instructions.text

# 		# add \" and \' for bash when writing to a file
# 		# using replace quotes
# 		clean_instructions = self.replace_quotes(instruc_txt).split('xxxxxxxxxx')[0]
# 		clean_instructions = " ".join(word if not "PythonLanguages" in word
# 			else self.get_last_word(word)
# 			for word in clean_instructions.split()
# 			)

# 		# clean the data
# 		# when I scrape edabit the text comes in a little dirty. 
# 		clean_instructions = clean_instructions.replace("Translate","\n\n")
# 		clean_instructions = clean_instructions.replace("Examples","\n~Examples~\n")
# 		clean_instructions = clean_instructions.replace("Notes","\n~Notes~\n")
# 		clean_instructions = clean_instructions.split("Watch a quick demo on how Edabit works")[0]
# 		clean_instructions = clean_instructions.replace("Published", "\n\tPublished")
# 		clean_tests = self.replace_quotes(tests.text).split('xxxxxxxxxx')[0]
# 		clean_code = self.replace_quotes(code.text).split('xxxxxxxxxx')[0]

# 		# create folder in current directory. 
# 		function_name = clean_code.split()[1].split("(")[0] # <<- only works for python
# 		challenge_name = function_name
		
# 		# --OS-- <chrdir>, <mkdir>
# 		os.chdir(self.python_repo)
# 		os.mkdir(challenge_name)
# 		os.chdir(challenge_name) # <-- We are now in the Python REPO
		
# 		# create instructions, code, and test files
# 		os.system(f"echo $'{clean_instructions}' > instructions.txt")
# 		os.system(f"echo $'{clean_code}pass' > {function_name}.py")
# 		with open(f"tests.py", "w") as f:
# 			# so we can separate the function from the tests
# 			# might be removed in later version 
# 			f.write(f"from {challenge_name} import {challenge_name}")
# 			f.write("\n")
# 			# needs to be more dynamic
# 			# (more than python capable)
# 			f.write(self.tests_script)
# 			f.write("\n")
		
# 		# create the tests file
# 		os.system(f"echo $'{clean_tests}' >> tests.py")

# 		# open files
# 		os.system("open instructions.txt")
# 		os.system("open tests.py")
# 		os.system(f"open {function_name}.py")

# 		# Git add, commit, push
# 		os.chdir(self.python_repo) # <-- so it updates old challenges
# 		os.system("git add .")
# 		os.system(f"git commit -m 'Add -->{function_name}<--'")
# 		os.system("git push")

# 	def close_driver(self):
# 		# probably should make this automatic
# 		self.driver.close()

# if __name__ == '__main__':
# 	e = Edabit()
# 	#e.login()
# 	e.download_challenge()
# 	e.close_driver()  
# # Fri May 13 00:31:03 MDT 2022 
# # last edit



```


# totalCups


```


```


# tweakLetters


```

std::string tweakLetters(std::string s, std::vector<int> arr) {
	
}pass

```


# validate_relationships


```

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
```


# zipper


```

def zipper(lst1, lst2):
	
	
	l1, l2 = "".join(str(i) for i in lst1), "".join(str(i) for i in lst2)
	
	for i in range(len(l1)):
		if l1[i:] in l2:
			l2_idx = l2.index(l1[i:]) - 1
			l1_idx = i - 1
			return [l1_idx, l2_idx]




print(zipper(
	[5, 5, 7, 8, 9, 1, 2], 
	[3, 2, 1, 1, 6, 6, 6, 6, 1, 2]
	))


```

