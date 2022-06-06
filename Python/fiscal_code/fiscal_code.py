conversion_table = {
  "0": (1, 0), "I": (19, 8),
  "1": (0, 1), "J": (21, 9),
  "2": (5, 2), "K": (2, 10),
  "3": (7, 3), "L": (4, 11),
  "4": (9, 4), "M": (18, 12),
  "5": (13, 5), "N": (20, 13),
  "6": (15, 6), "O": (11, 14),
  "7": (17, 7), "P": (3, 15),
  "8": (19, 8), "Q": (6, 16),
  "9": (21, 9), "R": (8, 17),
  "A": (1, 0), "S": (12, 18),
  "B": (0, 1), "T": (14, 19),
  "C": (5, 2), "U": (16, 20),
  "D": (7, 3), "V": (10, 21),
  "E": (9, 4), "W": (22, 22),
  "F": (13, 5), "X": (25, 23),
  "G": (15, 6), "Y": (24, 24),
  "H": (17, 7), "Z": (23, 25)
}



def fiscal_code(code):
	total = 0 
	odd = sum(conversion_table[i][0] 
		for j,i in enumerate(code) if (j+1) % 2)
	total += odd
	even = sum(conversion_table[i][1] 
		for j,i in enumerate(code) if not (j+1) % 2)
	total += even

	print(chr(total % 26 + 97).upper())
	return(chr(total % 26 + 97).upper())
	

fiscal_code("MRTMTT25D09F205")

