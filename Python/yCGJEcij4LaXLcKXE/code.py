
def get_price(dollar_amount):
    return int(dollar_amount.strip("$"))

def maximum_items(prices, budget):
    
    budget = get_price(budget)
    total = 0 
    item_count = 0 
    for price in sorted(map(get_price, prices)):
        if total + price <= budget:
            item_count += 1
            total += price
        else:
            break
    return item_count if item_count else "Not enough funds!"


class Test:
    def assert_equals(a,b):
        try:
            assert a == b
        except AssertionError:
            print(f"{a}\n > should equal \n\t{b}")
TestsConsoleTest = Test            

TestsConsoleTest.assert_equals(maximum_items(["$1", "$1", "$2"], "$3"), 2)
Test.assert_equals(maximum_items(["$10", "$7", "$2", "$60"], "$20"), 3)
Test.assert_equals(maximum_items(["$15", "$5", "$30", "$30", "$10"], "$2"), "Not enough funds!")
Test.assert_equals(maximum_items(["$99", "$8"], "$9"), 1)
Test.assert_equals(maximum_items(["$85", "$88", "$72", "$77", "$53"], "$56"), 1)
Test.assert_equals(maximum_items(["$12", "$2", "$49", "$21", "$76", "$64"], "$37"), 3)
Test.assert_equals(maximum_items(["$3", "$17", "$12", "$98", "$12", "$91", "$41", "$73"], "$116"), 5)
Test.assert_equals(maximum_items(["$18", "$16", "$32", "$30", "$43", "$80", "$13"], "$86"), 4)
Test.assert_equals(maximum_items(["$20", "$11", "$8", "$59", "$64", "$36", "$41", "$99", "$98"], "$357"), 8)
Test.assert_equals(maximum_items(["$12", "$98", "$56", "$88"], "$489"), 4)
Test.assert_equals(maximum_items(["$12"], "$26"), 1)
Test.assert_equals(maximum_items(["$65", "$78", "$78", "$61", "$51", "$91", "$76", "$27", "$85", "$70"], "$64"), 1)
Test.assert_equals(maximum_items(["$28", "$64"], "$404"), 2)
Test.assert_equals(maximum_items(["$69"], "$188"), 1)
Test.assert_equals(maximum_items(["$59", "$99", "$59", "$90", "$75", "$19", "$36", "$56", "$79", "$5"], "$74"), 3)
Test.assert_equals(maximum_items(["$73", "$7", "$75", "$33", "$7", "$95", "$11"], "$463"), 7)
Test.assert_equals(maximum_items(["$58", "$64", "$85", "$21", "$91", "$1"], "$333"), 6)
Test.assert_equals(maximum_items(["$89", "$7", "$27"], "$451"), 3)
Test.assert_equals(maximum_items(["$10", "$63", "$25", "$2", "$10", "$59", "$71", "$60", "$88"], "$129"), 5)
Test.assert_equals(maximum_items(["$23", "$82", "$75", "$17", "$67", "$67", "$95", "$48", "$15"], "$185"), 5)
Test.assert_equals(maximum_items(["$86", "$22", "$92", "$8", "$44", "$97"], "$102"), 3)
Test.assert_equals(maximum_items(["$16"], "$136"), 1)
Test.assert_equals(maximum_items(["$37", "$46", "$68", "$7", "$75", "$53", "$79"], "$20"), 1)
Test.assert_equals(maximum_items(["$71", "$36", "$5", "$56", "$33", "$66", "$91", "$49"], "$120"), 3)
Test.assert_equals(maximum_items(["$43", "$70", "$25", "$100", "$47", "$95", "$8"], "$66"), 2)
Test.assert_equals(maximum_items(["$70", "$11", "$87", "$65", "$6", "$9", "$63", "$55", "$90", "$95"], "$177"), 5)
Test.assert_equals(maximum_items(["$24", "$90", "$100", "$31", "$99"], "$287"), 4)
Test.assert_equals(maximum_items(["$34", "$62", "$62", "$98", "$100"], "$101"), 2)
Test.assert_equals(maximum_items(["$59", "$90", "$97", "$34", "$31", "$37", "$31", "$97", "$52", "$70"], "$224"), 5)
Test.assert_equals(maximum_items(["$29", "$71", "$23", "$27", "$46", "$33"], "$100"), 3)
Test.assert_equals(maximum_items(["$34", "$6"], "$263"), 2)
Test.assert_equals(maximum_items(["$36", "$34", "$74", "$90", "$14", "$21", "$96", "$24", "$67"], "$306"), 7)
Test.assert_equals(maximum_items(["$78", "$83"], "$239"), 2)
Test.assert_equals(maximum_items(["$6", "$8", "$67", "$64"], "$349"), 4)
Test.assert_equals(maximum_items(["$95", "$59", "$58", "$28", "$82", "$38", "$65", "$33", "$29"], "$247"), 6)
Test.assert_equals(maximum_items(["$57", "$97", "$47", "$91", "$70", "$78"], "$440"), 6)
Test.assert_equals(maximum_items(["$45"], "$319"), 1)
Test.assert_equals(maximum_items(["$5", "$89", "$78", "$73", "$44", "$93", "$57", "$80"], "$402"), 6)
Test.assert_equals(maximum_items(["$1", "$26", "$54", "$12", "$5", "$61"], "$47"), 4)
Test.assert_equals(maximum_items(["$16", "$50"], "$331"), 2)
Test.assert_equals(maximum_items(["$6", "$51"], "$88"), 2)
Test.assert_equals(maximum_items(["$74", "$91"], "$493"), 2)
Test.assert_equals(maximum_items(["$51", "$81", "$64", "$51"], "$47"), "Not enough funds!")
Test.assert_equals(maximum_items(["$32", "$60", "$12", "$93", "$82"], "$242"), 4)
Test.assert_equals(maximum_items(["$92", "$55", "$35", "$78", "$1"], "$421"), 5)
Test.assert_equals(maximum_items(["$46", "$41", "$47", "$52", "$99", "$62", "$50", "$62", "$65", "$38"], "$5"), "Not enough funds!")
Test.assert_equals(maximum_items(["$33", "$4", "$4"], "$475"), 3)
Test.assert_equals(maximum_items(["$78", "$11", "$37", "$95", "$60", "$11", "$53", "$58", "$97"], "$231"), 6)
Test.assert_equals(maximum_items(["$20", "$69", "$46", "$91", "$42", "$49", "$54", "$44", "$96"], "$476"), 8)
Test.assert_equals(maximum_items(["$60", "$42", "$93", "$47", "$67"], "$478"), 5)
Test.assert_equals(maximum_items(["$81", "$14", "$12", "$89", "$69"], "$377"), 5)
Test.assert_equals(maximum_items(["$16", "$67", "$76", "$78", "$72", "$19"], "$288"), 5)
Test.assert_equals(maximum_items(["$47", "$55", "$27", "$73", "$72"], "$461"), 5)