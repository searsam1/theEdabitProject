

def binary_to_text(n):
    decoded = ""
    for i in range(0,len(n), 8):
        decoded += chr( int( n[i:i+8], 2) )
    return decoded

def text_to_binary(word):
    res = "" 
    for i in word:
        res += (bin(ord(i)).lstrip("0b")).rjust(8,"0") 
    return res


words = "red", "green","blue"

for i in words:
    enc = text_to_binary(i)
    dec = binary_to_text(enc)
    print(enc, "➩",dec)