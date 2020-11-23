class BinaryTreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.value)


class BinaryTree:
    def __init__(self):
        self.root = None


def prefix_to_postfix(expression):
    exlist_prefix = expression.split(" ")
    extree = constructree_fromprefix_expression(exlist_prefix)
    exlist_postfix = []
    traverse_extree(extree.root, exlist_postfix)
    return " ".join(exlist_postfix)


def traverse_extree(node, exlist2):
    if node is None:
        return
    traverse_extree(node.left, exlist2)
    traverse_extree(node.right, exlist2)
    exlist2.append(node.value)


def constructree_fromprefix_expression(exlist):
    operators = {'*', '/', '-', '+'}
    stack = []
    tree = BinaryTree()
    for i in reversed(range(len(exlist))):
        if exlist[i] in operators:
            newnode = BinaryTreeNode(exlist[i])
            newnode.left = stack.pop()
            newnode.right = stack.pop()
            stack.append(newnode)
        else:
            stack.append(BinaryTreeNode(exlist[i]))
    tree.root = stack.pop()
    return tree

assert(prefix_to_postfix("5") == "5")
assert(prefix_to_postfix("+ 10 20") == "10 20 +")
assert(prefix_to_postfix("* + 1 2 - 5 3") == "1 2 + 5 3 - *")