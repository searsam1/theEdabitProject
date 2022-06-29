public class Pythagorean {	
	public static boolean isTriplet(int a, int b, int c) {
		
	}
}

TestsConsole/** 

================================= 

TestGen 3.1 for JUnit 4.13.0 		

Test Case: Pythagorean::isTriplet 

Timestamp: 09/21/2020 08:54:46 PM 

--------------------------------- 

® DARKKO 2020 © 

================================= 



**/ 



import static org.junit.Assert.assertEquals; 

import org.junit.Test; 



public class PythagoreanTest { 

	

	@Test

	public void test01() { 

		assertEquals(true, Pythagorean.isTriplet(3, 4, 5));

	}



	@Test

	public void test02() { 

		assertEquals(false, Pythagorean.isTriplet(1, 2, 3));

	}



	@Test

	public void test03() { 

		assertEquals(false, Pythagorean.isTriplet(3, 18, 8));

	}



	@Test

	public void test04() { 

		assertEquals(false, Pythagorean.isTriplet(7, 12, 7));

	}



	@Test

	public void test05() { 

		assertEquals(true, Pythagorean.isTriplet(13, 5, 12));

	}



	@Test

	public void test06() { 

		assertEquals(false, Pythagorean.isTriplet(12, 20, 18));

	}



	@Test

	public void test07() { 

		assertEquals(false, Pythagorean.isTriplet(17, 14, 2));

	}



	@Test

	public void test08() { 

		assertEquals(false, Pythagorean.isTriplet(6, 15, 12));

	}



	@Test

	public void test09() { 

		assertEquals(true, Pythagorean.isTriplet(60, 61, 11));

	}



	@Test

	public void test10() { 

		assertEquals(false, Pythagorean.isTriplet(7, 13, 15));

	}



	@Test

	public void test11() { 

		assertEquals(false, Pythagorean.isTriplet(12, 18, 7));

	}



	@Test

	public void test12() { 

		assertEquals(true, Pythagorean.isTriplet(8, 17, 15));

	}



	@Test

	public void test13() { 

		assertEquals(true, Pythagorean.isTriplet(3120, 79, 3121));

	}



	@Test

	public void test14() { 

		assertEquals(true, Pythagorean.isTriplet(72, 54, 90));

	}



	@Test

	public void test15() { 

		assertEquals(true, Pythagorean.isTriplet(80, 48, 64));

	}



}

// end of tests