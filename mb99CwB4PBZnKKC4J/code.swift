func license(_ me: String, _ agents: Int, _ others: String) -> Int {
	
}

func license(_ me: String, _ agents: Int, _ others: String) -> Int {2  3}

import XCTest​class SolutionTest: XCTestCase {    static var allTests = [    ("Test 1", test1),    ("Test 2", test2),    ("Test 3", test3),    ("Test 4", test4),    ("Test 5", test5)    ]​  func test1() {    XCTAssertEqual(license("Zebediah", 1, "Bob Jim Becky Pat"), 100)  }​  func test2() {    XCTAssertEqual(license("Eric", 2, "Adam Caroline Rebecca Frank"), 40)  }​  func test3() {    XCTAssertEqual(license("Aaron", 3, "Jane Max Olivia Sam"), 20)  }​  func test4() {    XCTAssertEqual(license("Zebediah", 4, "Bob Jim Becky Pat"), 40)  }