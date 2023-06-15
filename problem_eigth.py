'''
Dada una lista de números en orden ascendente y un número objetivo, 
escribe una función recursiva que encuentre si el número objetivo está en la lista utilizando una búsqueda binaria.
'''
import unittest

def binary_search_recursive(arr, target):
    if not arr:
        return False

    mid = len(arr) // 2
    if arr[mid] == target:
        return True
    elif arr[mid] > target:
        return binary_search_recursive(arr[:mid], target)
    else:
        return binary_search_recursive(arr[mid+1:], target)
    
class TestBinarySearchRecursive(unittest.TestCase):
    def test_binary_search_recursive(self):
        arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        target1 = 5
        self.assertTrue(binary_search_recursive(arr1, target1))

        arr2 = [1, 2, 3, 4, 6, 7, 8, 9, 10]
        target2 = 5
        self.assertFalse(binary_search_recursive(arr2, target2))

        arr3 = []
        target3 = 5
        self.assertFalse(binary_search_recursive(arr3, target3))
        
        arr4 = [5]
        target4 = 5
        self.assertTrue(binary_search_recursive(arr4, target4))
        
if __name__ == '__main__':
    unittest.main()