'''
Question 4

Find the least common ancestor between two nodes on a binary search tree. The least common ancestor is the farthest node from the root that is an ancestor of both nodes. For example, the root is a common ancestor of all nodes on the tree, but if both nodes are descendents of the root's left child, then that left child might be the lowest common ancestor.
You can assume that both nodes are in the tree, and the tree itself adheres to all BST properties.
The function definition should look like question4(T, r, n1, n2), where T is the tree represented as a matrix, where the index of the list is equal to the integer stored in that node and a 1 represents a child node, r is a non-negative integer representing the root, and n1 and n2 are non-negative integers representing the two nodes in no particular order. For example, one test case might be

question4([[0, 1, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [1, 0, 0, 0, 1],
           [0, 0, 0, 0, 0]],
          3,
          1,
          4)

and the answer would be 3.
'''

def ques4(T, r, n1, n2):
    while n1 != r and n2 = r:
        n1 = parent(T, r, n1)  # O(n)
        n2 = parent(T, r, n2)

        if n1 == n2:
            return n2

    return r



def parent(T, r, n):
	#return parent of n if it exists, otherwise return -1
    numrows = len(T) - 1

    if T[r][n] == 1:
        return r
    else:

        if r > n:
            # left to right tree traversal

            i = 0
            while i <= numrows:
                if T[i][n] == 1:
                    return i
                i += 1

        elif r < n:
            #  right to left tree traversal

            i = numrows
            while i >= 0:
                if T[i][n] == 1:
                    return i
                i -= 1

        else:
            return r


    return -1


print ques4([[0,1,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[1,0,0,0,1],[0,0,0,0,0]],3,1,4)
print ques4([[0,1,0,0,0,1],[0,0,0,0,0,0],[0,0,0,0,0,0],[1,0,0,0,1,0],[0,0,0,0,0,0],[0,0,0,0,0,0]],3,1,5)
print ques4([[0,1,0,0,0,1,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[1,0,0,0,1,0,0],[0,0,0,0,0,0,0],[0,0,1,0,0,0,1],[0,0,0,0,0,0,0]],3,2,6)
# O(n^2)
