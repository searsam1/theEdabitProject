public class SideLengths {
  public static double[] otherSides(int n) {
		
  }
}

TestsConsoleimport static org.junit.Assert.assertArrayEquals; 

import org.junit.Test; 



public class SideLengthsTest {

	@Test

	public void test01() { 

		assertArrayEquals(new double[] {2, 1.73}, SideLengths.otherSides(1), 6);

	}



	@Test

	public void test02() { 

		assertArrayEquals(new double[] {24, 20.78}, SideLengths.otherSides(12), 6);

	}



	@Test

	public void test03() { 

		assertArrayEquals(new double[] {6, 5.2}, SideLengths.otherSides(3), 6);

	}



	@Test

	public void test04() { 

		assertArrayEquals(new double[] {10, 8.66}, SideLengths.otherSides(5), 6);

	}



	@Test

	public void test05() { 

		assertArrayEquals(new double[] {14, 12.12}, SideLengths.otherSides(7), 6);

	}



	@Test

	public void test06() { 

		assertArrayEquals(new double[] {34, 29.44}, SideLengths.otherSides(17), 6);

	}

	

	@Test

	public void test07() { 

		int r = SCTC.randomInt(0b101, 0x63);

		assertArrayEquals(new double[] {SCTC.adhc(r), SCTC.odhs(SCTC.adhc(r))}, SideLengths.otherSides(r), 6);

	}

	

	@Test

	public void test08() { 

		int r = SCTC.randomInt(0b101, 0x63);

		assertArrayEquals(new double[] {SCTC.adhc(r), SCTC.odhs(SCTC.adhc(r))}, SideLengths.otherSides(r), 6);

	}

	

	@Test

	public void test09() { 

		int r = SCTC.randomInt(0b101, 0x63);

		assertArrayEquals(new double[] {SCTC.adhc(r), SCTC.odhs(SCTC.adhc(r))}, SideLengths.otherSides(r), 6);

	}

	

	@Test

	public void test10() { 

		int r = SCTC.randomInt(0b101, 0x63);

		assertArrayEquals(new double[] {SCTC.adhc(r), SCTC.odhs(SCTC.adhc(r))}, SideLengths.otherSides(r), 6);

	}

	

	@Test

	public void test11() { 

		int r = SCTC.randomInt(0b101, 0x63);

		assertArrayEquals(new double[] {SCTC.adhc(r), SCTC.odhs(SCTC.adhc(r))}, SideLengths.otherSides(r), 6);

	}

	

	@Test

	public void test12() { 

		int r = SCTC.randomInt(0b101, 0x63);

		assertArrayEquals(new double[] {SCTC.adhc(r), SCTC.odhs(SCTC.adhc(r))}, SideLengths.otherSides(r), 6);

	}

}





























































class SCTC {

	public static int randomInt(int... i) {

		return (int)(Math.random()*((i[01]-i[00])+0b1))+i[0x0];

	}

	

	public static int adhc(int b) {

		return (int)(b/StrictMath.cos(Math.toRadians(0x3c/074*0b111100))+0b0001);

	}

	

	public static double odhs(int c) {

		return Math.round(StrictMath.sin(((074*0b0001)*Math.PI)/(0x3c*3))*c*100.0)/100.0;

	}

}