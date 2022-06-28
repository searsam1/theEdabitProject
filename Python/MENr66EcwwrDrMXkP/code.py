import itertools
def permutations(s):
    res = " ".join( 
		sorted(
		list(
		map(
		lambda x : "".join(x),
    	itertools.permutations(s, len(s))
	))))
    return res