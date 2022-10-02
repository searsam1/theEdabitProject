function totalAmountAdjectives(obj) {
	
}...

TestsConsoleconst obj = { a: "moron" }
const obj2 = { a: "moron", b: "scumbag", c: "moron", d: "dirtbag" } 
const obj3 = {b: "scumbag", c: "moron", d: "dirtbag" } 
let dynamic = {}
const random = Test.randomNumber()
let arr = new Array(random).fill(".")
arr.forEach((item, i) => dynamic[i] = item)

Test.assertEquals(totalAmountAdjectives(obj), 1)
Test.assertEquals(totalAmountAdjectives(obj2), 4)
Test.assertEquals(totalAmountAdjectives(obj3), 3)
Test.assertEquals(totalAmountAdjectives(dynamic), random)