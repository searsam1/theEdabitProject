# Mirror Cipher
<br><br>
## Mubashir Hassan 
<br><br>
### """In Mirror Cipher, encoding is done by switching message characters with its mirror opposite character of the key.
Create a function that takes two arguments; a message and an optional key, and return the encoded message.
There are some variations on the rules of encipherment. One version of the cipher rules are outlined below:
Step 1: Replace all characters of the given message with mirror character in the key:
Step 2: Return encoded message in lower case:
If optional key is not given, consider the whole alphabet as a default (i.e. key = "abc..z").
Ignore case of message and key, (e.g. "M" = "m")."""
<br><br>
[auLEvdvBT5PRnALvn](https://edabit.com/challenge/auLEvdvBT5PRnALvn)
<br><br>
```message = "Mubashir Hassan"
key = "edabitisamazing"

mirror_cipher(message, key) ➞ "tuzishar hissid"
```

<br><br>

> Ignoring case, M is present in the key at index position 9. The mirror character is the character in the key which is the same distance from the end of the key (counting backwards). The mirror character is therefore at index position 5 - which is t.

> The second character is not in the key so is not transposed.

> The third character, b, is at index 3. It's mirror is at index 11 - which is z.

