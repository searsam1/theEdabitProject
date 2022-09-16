def best_words(lst):
	...

class Test:
    def assert_equals(a,b):
        try:
            assert a == b
        except AssertionError:
            print(f"{a}\n > should equal \n\t{b}")
TestsConsoleTest = Test            

TestsConsoleTest.assert_equals(best_words(['got','test','oh','sat','rents']),['oh','rents'])
Test.assert_equals(best_words(['digest','divest','verge','honey','money']),['honey'])
Test.assert_equals(best_words(['wig','jury','interim','size','hunter']),['jury'])
Test.assert_equals(best_words(['berry','whiz','laughed','ghetto','psychic']),['whiz', 'psychic'])
Test.assert_equals(best_words(['library','index','memory','ghosts','quit']),['library','index','memory','quit'])
Test.assert_equals(best_words(['singing','swine','llamas','crunchy','creamy']),['crunchy'])