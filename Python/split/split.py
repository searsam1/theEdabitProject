import re


def split(word):
	p = "[aeiou]+|[^aeiou]"
	matches = re.findall(p,word)
	return matches


word = "beautifully"
split(word)

