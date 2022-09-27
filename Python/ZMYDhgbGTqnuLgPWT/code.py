from itertools import combinations
def triplet_sum(lst, n):
    combos = list(combinations(lst, 3))
    s = map(sum,combos)
    print(list(s).count(n))

triplet_sum([6, 2, 6, 0, 9, 2, 5, 8], 20)


