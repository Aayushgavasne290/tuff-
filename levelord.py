
class Node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None


class BST:
    def _init_(self):
        self.root = None
        self.cnt = 0
        self.lcnt = 0
        self.nlcnt = 0

    def insert(self, new_node):
        if self.root is None:  # BST is empty
            self.root = new_node
        else:
            temp = self.root
            while True:
                if new_node.data < temp.data:  # left subtree
                    if temp.left is None:
                        temp.left = new_node
                        return
                    else:
                        temp = temp.left
                else:  # right subtree
                    if temp.right is None:
                        temp.right = new_node
                        return
                    else:
                        temp = temp.right

    def del_node(self, rt, val):
        if rt is None:
            return rt
        if val<rt.data:
            rt.left=self.del_node(rt.left, val)
        elif val>rt.data:
            rt.right=self.del_node(rt.right, val)
        else:
            if rt.left is None: #Node with right child only
                return rt.right
            if rt.right is None: #Node with left child only
                return rt.left
            #Node has both left and right children
            succ=self.get_successor(rt)
            rt.data=succ.data
            rt.right=self.del_node(rt.right, succ.data)
        return rt

    def get_successor(self, temp):
        temp=temp.right
        while temp.left is not None:
            temp=temp.left
        return temp

    def inorder(self, rt):
        if rt is None:
            return
        else:
            self.inorder(rt.left)
            print(rt.data, end=" ")
            if rt.left is None and rt.right is None:
                self.lcnt += 1
            else:
                self.nlcnt += 1
            self.cnt += 1
            self.inorder(rt.right)
