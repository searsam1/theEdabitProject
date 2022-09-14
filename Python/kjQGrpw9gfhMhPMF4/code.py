
def check_pal(s):
    return s[::-1] == s

check_pal("189989881")
check_pal("abccba")

def palindrome_set(lst):
    scores = []
    for word in lst:
        chars = "".join(i for i in word if i.isalpha())
        print(chars)
        nums = "".join(i for i in word if i.isnumeric())
        print(nums)
        score = check_pal(nums) + check_pal(chars)
        scores.append(score)
    return scores
print(
    palindrome_set(["18a99b89cc881ba", "p7o8p987", "p7o", "p7o8"])
)