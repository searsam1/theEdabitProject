
#Test.assert_equals(tree_photography([1, 2, 3, 6, 5]), "left")

# If I stand on the left, I can see trees of heights 1, 3 and 6.
# If I stand on the right, I can see trees of heights 5 and 6.
# Return "left" because I would see more trees.

def tree_photography(trees):

    biggest,biggest_r = [],[] 
    for tree, tree_r in zip(trees, trees[::-1]):
        if all(tree > i for i in biggest):
            biggest.append(tree)
        if all(tree_r > i for i in biggest_r):
            biggest_r.append(tree_r)

    return ["left","right"][len(biggest_r) > len(biggest)]
	
res = tree_photography(
    [1, 2, 3, 6, 5]
    )
print(res)