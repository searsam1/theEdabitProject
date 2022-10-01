function spaceMeOut(str) {
	
}...

TestsConsoleTest.assertEquals(spaceMeOut("space"), "s p a c e", "Example #1")
Test.assertEquals(spaceMeOut("far out"), "f a r   o u t", "Example #2")
Test.assertEquals(spaceMeOut("elongated musk"), "e l o n g a t e d   m u s k", "Example #3")
Test.assertEquals(spaceMeOut("long"), "l o n g")
Test.assertEquals(spaceMeOut("123"), "1 2 3")
Test.assertEquals(spaceMeOut("a1b2c3"), "a 1 b 2 c 3")

// made by @Joshua Señoron