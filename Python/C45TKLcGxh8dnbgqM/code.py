def caesar_cipher(s, k):
	...

class Test:
    def assert_equals(a,b):
        try:
            assert a == b
        except AssertionError:
            print(f"{a}\n > should equal \n\t{b}")
TestsConsoleTest = Test            

TestsConsoleTest.assert_equals(caesar_cipher("middle-Outz", 2), "okffng-Qwvb")
Test.assert_equals(caesar_cipher("Always-Look-on-the-Bright-Side-of-Life", 5), "Fqbfdx-Qttp-ts-ymj-Gwnlmy-Xnij-tk-Qnkj")
Test.assert_equals(caesar_cipher("A friend in need is a friend indeed", 20), "U zlcyhx ch hyyx cm u zlcyhx chxyyx")
Test.assert_equals(caesar_cipher("A Fool and His Money Are Soon Parted.", 27), "B Gppm boe Ijt Npofz Bsf Tppo Qbsufe.")
Test.assert_equals(caesar_cipher("One should not worry over things that have already happened and that cannot be changed.", 49), "Lkb pelria klq tloov lsbo qefkdp qexq exsb xiobxav exmmbkba xka qexq zxkklq yb zexkdba.")
Test.assert_equals(caesar_cipher("Back to Square One is a popular saying that means a person has to start over, similar to: back to the drawing board.", 126), "Xwyg pk Omqwna Kja eo w lklqhwn owuejc pdwp iawjo w lanokj dwo pk opwnp kran, oeiehwn pk: xwyg pk pda znwsejc xkwnz.")