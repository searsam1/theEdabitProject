class Node:
    tree=[]

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data
				# Hint this line to clear the list for every object
        Node.tree.clear()

    def insert(self, data):
		#code
		
    def PrintTree(self):
      #code



TestsConsoleroot = Node(10)

root.insert(5)

root.insert(3)

root.insert(12)

root.insert(13)

root.insert(11)

root.insert(6)

Test.assert_equals(root.PrintTree(), [3, 5, 6, 10, 11, 12, 13])

Test.assert_equals(root.data, 10)

Test.assert_equals(root.left.data, 5)

Test.assert_equals(root.left.left.data, 3)

Test.assert_equals(root.left.right.data, 6)

Test.assert_equals(root.right.data, 12)

Test.assert_equals(root.right.left.data, 11)

Test.assert_equals(root.right.right.data, 13)



root2 = Node(15)

root2.insert(7)

root2.insert(5)

root2.insert(18)

root2.insert(17)

root2.insert(9)

root2.insert(19)

Test.assert_equals(root2.PrintTree(), [5, 7, 9, 15, 17, 18, 19])

Test.assert_equals(root2.data, 15)

Test.assert_equals(root2.left.data, 7)

Test.assert_equals(root2.left.left.data, 5)

Test.assert_equals(root2.left.right.data, 9)

Test.assert_equals(root2.right.data, 18)

Test.assert_equals(root2.right.left.data, 17)

Test.assert_equals(root2.right.right.data, 19)





root3 = Node(8)

root3.insert(10)

root3.insert(3)

root3.insert(6)

root3.insert(14)

root3.insert(1)

root3.insert(4)

root3.insert(13)

root3.insert(7)

Test.assert_equals(root3.PrintTree(), [1, 3, 4, 6, 7, 8, 10, 13, 14])

Test.assert_equals(root3.data, 8)

Test.assert_equals(root3.left.data, 3)

Test.assert_equals(root3.left.left.data, 1)

Test.assert_equals(root3.left.right.data, 6)

Test.assert_equals(root3.right.data, 10)

Test.assert_equals(root3.right.right.data, 14)

Test.assert_equals(root3.right.right.left.data, 13)

Test.assert_equals(root3.left.right.left.data, 4)

Test.assert_equals(root3.left.right.right.data, 7)