public class Challenge {
  public static String fizzBuzz(int n) {
		public class Challenge {
     public static String fizzBuzz(int n) {
      return n % 15 == 0 ? "FizzBuzz" : 
        n % 5 == 0 ? "Buzz" : 
          n % 3 == 0 ? "Fizz" : 
            String.format("%d", n);
  }
}
  }
}

TestsConsoleimport org.junit.Test;

import static org.junit.Assert.assertEquals;



public class Tests {

  @Test

  public void test1() {

	assertEquals(Challenge.fizzBuzz(3), "Fizz");

  }

  @Test

  public void test2() {

	assertEquals(Challenge.fizzBuzz(5), "Buzz");

  }

  @Test

  public void test3() {

	assertEquals(Challenge.fizzBuzz(15), "FizzBuzz");

  }

  @Test

  public void test4() {

	assertEquals(Challenge.fizzBuzz(10), "Buzz");

  }

  @Test

  public void test5() {

	assertEquals(Challenge.fizzBuzz(98), "98");

  }

}