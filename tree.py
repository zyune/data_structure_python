class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def printTreerear(self):
        if self.left:
            self.left.printTreerear()
        print(self.data)
        if self.right:
            self.right.printTreerear()

    # 先续深度遍历 DFS recursion Preorder
    def print_tree_recursion_Preorder(self):
        print(self.data)
        if self.left:
            self.left.print_tree_recursion_Preorder()
        if self.right:
            self.right.print_tree_recursion_Preorder()

    # middle aorder
    def print_tree_recursion_Midorder(self):

        if self.left:
            self.left.print_tree_recursion_Midorder()
        print(self.data)
        if self.right:
            self.right.print_tree_recursion_Midorder()

    def print_tree_recursion_Postorder(self):
        if self.left:
            self.left.print_tree_recursion_Postorder()
        if self.right:
            self.right.print_tree_recursion_Postorder()
        print(self.data)

    def printselfdata(self):
        print(self.data)


def depth_first_values(root):
    stack = [root]
    result = []
    while len(stack) > 0:
        current = stack.pop()
        result.append(current)
        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)

    return result


a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")
a.left = b
a.right = c
b.left = d
b.right = e
c.right = f


a.print_tree_recursion_Preorder()
print("\n")
a.print_tree_recursion_Midorder()
print("\n")
a.print_tree_recursion_Postorder()

