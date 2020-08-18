# Input:
#         1
#       /   \
#      2     3
#     / \   / \
#    4   5 6   7
#
# Output: [1, 3, 2, 4, 5, 6, 7]

# Here's some starter code

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def zigzag_order(tree):
    other_list = [tree.value]
    level = 1

    if tree.left is None:
        return None
    else:
        level += 1
        left = tree.left
        right = tree.right
        if level % 2 == 0:
            other_list[1:2] = [right.value, left.value]
            if left.left is None:
                return None
            else:
                level += 1
                deep_left = (left.left, left.right)
                deep_right = (right.left, right.right)
                if level % 2 == 1:
                    for n, i in zip(deep_left, deep_right):
                        other_list.append(n.value)
                        other_list.append(i.value)

    return other_list








    # otherList = []
    # level = 1
    # left = tree.left
    # right = tree.right
    # otherList.append(tree.value)
    #
    # if left and right is Node:
    #     level += 1
    #     if level == 2:
    #         otherList[1:2] = [left.value, right.value]
        
    # left = tree.left
    # right = tree.right
    # tree_l = [tree.value,
    #           right.value,
    #           left.value,
    #           left.left.value,
    #           left.right.value,
    #           right.left.value,
    #           right.right.value]
    # return tree_l


n4 = Node(4)
n5 = Node(5)
n6 = Node(6)
n7 = Node(7)
n2 = Node(2, n4, n5)
n3 = Node(3, n6, n7)
n1 = Node(1, n2, n3)

print(zigzag_order(n1))
# [1, 3, 2, 4, 5, 6, 7]
