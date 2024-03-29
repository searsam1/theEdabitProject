

def un_bunch(d):
    quantity = d["quantity"]
    d["quantity"] = 1
    d2 = [ d for _ in range(quantity) ] 
    return d2

def split_bunches(bunches):
    return sum(map(un_bunch, bunches),[])
    

class Test:
    def assert_equals(a,b):
        try:
            assert a == b
        except AssertionError:
            print(f"{a}\n > should equal \n\t{b}")
TestsConsoleTest = Test            

TestsConsoleTest.assert_equals(split_bunches([{ "name": 'bananas', "quantity": 1 }]), [{ "name": 'bananas', "quantity": 1 }])
Test.assert_equals(split_bunches([{ "name": 'bananas', "quantity": 2 }, { "name": 'grapes', "quantity": 2 }]), [{ "name": 'bananas', "quantity": 1 }, { "name": 'bananas', "quantity": 1 }, { "name": 'grapes', "quantity": 1 }, { "name": 'grapes', "quantity": 1 }])
Test.assert_equals(split_bunches([{ "name": 'cherry tomatoes', "quantity": 3}, { "name": 'bananas', "quantity": 1 }, { "name": 'grapes', "quantity": 2 }, { "name": 'cherry tomatoes', "quantity": 3}]), [{ "name": 'cherry tomatoes', "quantity": 1}, { "name": 'cherry tomatoes', "quantity": 1}, { "name": 'cherry tomatoes', "quantity": 1}, { "name": 'bananas', "quantity": 1 }, { "name": 'grapes', "quantity": 1 }, { "name": 'grapes', "quantity": 1 }, { "name": 'cherry tomatoes', "quantity": 1}, { "name": 'cherry tomatoes', "quantity": 1}, { "name": 'cherry tomatoes', "quantity": 1}])
Test.assert_equals(split_bunches([{ "name": "currants", "quantity": 1 }, {"name": "grapes", "quantity": 2 }, {"name": "bananas", "quantity": 2 }]), [{"name": "currants", "quantity": 1},{"name": "grapes", "quantity": 1 },{"name": "grapes", "quantity": 1 },{"name": "bananas", "quantity": 1 },{"name": "bananas", "quantity": 1 }])