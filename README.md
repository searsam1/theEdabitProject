# theEdabitProject
Store of Edabit Challenges.

### Below Is a collection of all the python challenges in the repository
### I got them with this Python Script:
```
from string import punctuation
import clipboard
import os

path = "/Users/111244rfsf/Documents/Repositories/theEdabitProject/theEdabitProjectRepo/Python"

os.system(f"cd {path}")
os.system(f"ls | pbcopy")

folders = clipboard.paste()
"""
...
multiply_matrix
nom_nom
prime_count
python_collect.py
...
"""

folders = [i for i in folders.split("\n") if not "." in i
and i
]

# Reset Gallery
os.system("echo > gallery.md")
for folder in folders:
	os.system(f"echo '\n# {folder}\n' >> gallery.md")
	os.system("echo '\n```\n' >> gallery.md")
	os.system(f"cat {folder}/{folder}.py >> gallery.md")
	os.system("echo '\n```\n' >> gallery.md")
print("done.")

with open("gallery.md", "r") as f:
	gallery = f.read()

with open("fancy_md_gallery.md", "w") as f:
	f.write(gallery)
```

# addition


```

def addition(num):
	pass

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


# sort_by_answer


```

def sort_by_answer(lst):
	key_func = lambda i : eval(i.replace("x", "*"))
	return sorted(lst,key=key_func)
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
