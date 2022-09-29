# Injection II: Using Eval
<br><br>
## bangyen
<br><br>
### """The bookstore from this collection, in a desperate attempt to avoid getting hacked, changed from exec() to eval(). Create a query that stores the users dictionary in the res variable.
Create a string, not a function.
The site dictionary and search function have been gutted/deleted for brevity."""
<br><br>
[nsAkCCkh2fyW3fhPG](https://edabit.com/challenge/nsAkCCkh2fyW3fhPG)
<br><br>
```param = "your text here"

users = {
  "user1": "password",
  "user2": "password"
}

res = eval('search("%s")' % param)

print(res) ➞ users
```

<br><br>
