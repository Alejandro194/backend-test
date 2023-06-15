'''
Escribe una función llamada remove_duplicates que acepte una lista como parámetro 
y devuelva una nueva lista sin elementos duplicados
'''

def remove_duplicates(lst):
    return list(set(lst))

import unittest

def remove_duplicates(lst):
    return list(set(lst))

class TestRemoveDuplicates(unittest.TestCase):
    def test_remove_duplicates(self):
        lst1 = [1, 2, 3, 4, 5]
        self.assertEqual(remove_duplicates(lst1), [1, 2, 3, 4, 5])

        lst2 = [1, 2, 2, 3, 3, 3, 4, 5, 5]
        self.assertEqual(remove_duplicates(lst2), [1, 2, 3, 4, 5])

        lst3 = []
        self.assertEqual(remove_duplicates(lst3), [])
        
        
if __name__ == '__main__':
    unittest.main()