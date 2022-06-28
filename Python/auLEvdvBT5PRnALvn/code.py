import string
def mirror_cipher(message, key=string.ascii_lowercase):
    """
    Example:
    
    message = "Mubashir Hassan"
    key = "edabitisamazing"

    mirror_cipher(message, key) ➞ "tuzishar hissid"
    """
    
    message = message.lower()
    key=key.lower()

    digest = "" 

    for char in message:
        if char in key:
            idx = key[::-1].index(char)
            digest += key[idx]
        else:
            digest += char
    return digest



message = "Mubashir Hassan"
key = "edabitisamazing"

mirror_cipher(message, key) # == "tuzishar hissid"


class Test():
    def assert_equals(a,b,message=None):
        try:
            assert a == b
        except AssertionError:
            print("FAIL")

Test.assert_equals(mirror_cipher("Airforce is best", "pilot"), "aorfirce os besp")

Test.assert_equals(mirror_cipher("hello"), "svool")

Test.assert_equals(mirror_cipher("goodbye"), "tllwybv")

Test.assert_equals(mirror_cipher("ngmlsoor"), "mtnohlli")

Test.assert_equals(mirror_cipher("gsrh rh z hvxivg"), "this is a secret")

Test.assert_equals(mirror_cipher("hello", "abcdefgh"), "adllo")

Test.assert_equals(mirror_cipher("goodbye", ""), "goodbye")

Test.assert_equals(mirror_cipher("this is a secret", " *"), "this*is*a*secret")

