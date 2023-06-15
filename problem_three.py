'''
Escribe una clase llamada BinaryTree que implemente un árbol binario de búsqueda. 
La clase debe tener métodos para insertar, buscar, y debe ser capaz de imprimir el árbol en orden ascendente.
'''

class BinaryTree:
    class Node:
        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None

    def insert(self, value):
        node = self.Node(value)
        if self.root is None:
            self.root = node
        else:
            current = self.root
            while True:
                if value < current.value:
                    if current.left is None:
                        current.left = node
                        break
                    else:
                        current = current.left
                else:
                    if current.right is None:
                        current.right = node
                        break
                    else:
                        current = current.right

    def search(self, value):
        current = self.root
        while current is not None:
            if value == current.value:
                return True
            elif value < current.value:
                current = current.left
            else:
                current = current.right
        return False

    def inorder_traversal(self, node):
        if node is not None:
            self.inorder_traversal(node.left)
            print(node.value, end=" ")
            self.inorder_traversal(node.right)

    def print_inorder(self):
        self.inorder_traversal(self.root)


import unittest

class TestBinaryTree(unittest.TestCase):
    
    def test_insert(self):
        values = [8,3,10,1]
        tree = BinaryTree()

        for value in values:
            tree.insert(value)
        self.assertEqual(tree.root.value, 8)
        self.assertEqual(tree.root.left.value, 3)
        self.assertEqual(tree.root.left.left.value, 1)
        self.assertEqual(tree.root.right.value, 10)

    def test_search(self):
        values = [8,3,10,1]
        tree = BinaryTree()
        
        for value in values:
            tree.insert(value)
        
        self.assertTrue(tree.search(3))
        self.assertTrue(tree.search(10))
        self.assertFalse(tree.search(5))
        self.assertFalse(tree.search(0))

    def test_print_inorder(self):
        values = [8,3,10,1,6,14,4,7,13]
        tree = BinaryTree()
        for value in values:
            tree.insert(value)
        

        import io
        import sys
        sys.stdout = io.StringIO()

        tree.print_inorder()
        self.assertEqual(sys.stdout.getvalue().strip(), "1 3 4 6 7 8 10 13 14")

        sys.stdout = sys.__stdout__

if __name__ == '__main__':
    unittest.main()