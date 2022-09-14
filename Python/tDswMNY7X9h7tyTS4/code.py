def morse(txt):
    d = {"A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".",
         "F": "..-.", "G": "--.", "H": "....", "I": "..", "J": ".---",
         "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---",
         "P": ".--.", "Q": "--.-", "R": ".-.", "S": "...", "T": "-",
         "U": "..-", "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--", "Z": "--..",
         " ": "....."}
    if not "." in txt:
        d = {ord(k): v + " " for k, v in d.items()}
        txt = txt.upper().translate(d)
        return txt.strip()
    else:
        words = txt.split(".....")
        d = {v: k for k, v in d.items()}
        words = [i.split() for i in words]

        new_words = []
        for word in words:
            new_word = ""
            for letter in word:
                letter = d[letter]
                new_word += letter
            new_words.append(new_word)
        translation = " ".join(new_words)
        return translation
res = morse("I made a program to write morse code for me")
res2 = morse(".. ..... -- .- -.. . ..... .- ..... .--. .-. --- --. .-. .- -- ..... - --- ..... .-- .-. .. - . ..... -- --- .-. ... . ..... -.-. --- -.. . ..... ..-. --- .-. ..... -- .")
print(res, res2, sep="\n->\n")
