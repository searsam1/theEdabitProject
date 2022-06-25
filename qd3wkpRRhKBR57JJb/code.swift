func fizzBuzz(_ num: Int) -> String {

}


TestsConsoleimport XCTest



class SolutionTest: XCTestCase {

    static var allTests = [

        ("Test 1", test1),

        ("Test 2", test2),

        ("Test 3", test3),

        ("Test 4", test4),

        ("Test 5", test5)

    ]



    func test1() {

         XCTAssertEqual(fizzBuzz(3), "Fizz")

    }



    func test2() {

        XCTAssertEqual(fizzBuzz(5), "Buzz")

    }



    func test3() {

        XCTAssertEqual(fizzBuzz(15), "FizzBuzz")

    }



    func test4() {

        XCTAssertEqual(fizzBuzz(10), "Buzz")

    }



    func test5() {

        XCTAssertEqual(fizzBuzz(98), "98")

    }

}



XCTMain([

    testCase(SolutionTest.allTests)

])