
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
	