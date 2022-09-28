def recur_index(txt):
	...

class Test:
    def assert_equals(a,b):
        try:
            assert a == b
        except AssertionError:
            print(f"{a}\n > should equal \n\t{b}")
TestsConsoleTest = Test            

TestsConsolestr_vectors, obj_res = [
    'DXTDXTXDTXD', 'YXZXYTUVXWV', 'YZTTZMNERXE',
    'AREDCBSDERD', '', None, 'KDXTDATTDDX',
    'AKEDCBERSDA', 'DXKETRETXDK', 'ABCKPEPGBCG',
    'KLMNONMLKOP', 'ABCDEFGHIJK', 'ABCDEFGABCD', None], [
    {"D": [0, 3]}, {"X": [1, 3]}, {"T": [2, 3]},
    {"D": [3, 7]}, {}, {}, {"D": [1, 4]},
    {"E": [2, 6]}, {"E": [3, 6]}, {"P": [4, 6]},
    {"N": [3, 5]}, {}, {"A": [0, 7]}, {}
]
for i, s in enumerate(str_vectors):
  Test.assert_equals(recur_index(s), obj_res[i])