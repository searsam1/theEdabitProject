def mirror_cipher(message):
	

TestsConsoleTest.assert_equals(mirror_cipher("Mubashir Hassan", "edabitisamazing"), "tuzishar hissid")

Test.assert_equals(mirror_cipher("Matt MacPherson"), "nzgg nzxksvihlm")

Test.assert_equals(mirror_cipher("Airforce is best", "pilot"), "aorfirce os besp")

Test.assert_equals(mirror_cipher("hello"), "svool")

Test.assert_equals(mirror_cipher("goodbye"), "tllwybv")

Test.assert_equals(mirror_cipher("ngmlsoor"), "mtnohlli")

Test.assert_equals(mirror_cipher("gsrh rh z hvxivg"), "this is a secret")

Test.assert_equals(mirror_cipher("hello", "abcdefgh"), "adllo")

Test.assert_equals(mirror_cipher("goodbye", ""), "goodbye")

Test.assert_equals(mirror_cipher("this is a secret", " *"), "this*is*a*secret")

# Mubashir