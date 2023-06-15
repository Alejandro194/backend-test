'''
En circunstancias donde el segundo listado sea también grande es conveniente procesar las peticiones en paralelo; 
en este escenario sería conveniente poder configurar una máxima cantidad de workers 
para que procesen de forma paralela el segundo arreglo. 
Proponga una solución general a este problema utilizando Python3.
'''

import unittest
from multiprocessing import Pool

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

def binary_search_wrapper(args):
    arr, target = args
    return binary_search_recursive(arr, target)

def map_binary_search(lst1, lst2, max_workers=None):
    if max_workers is None:
        return list(map(lambda x: binary_search_recursive(lst1, x), lst2))
    else:
        with Pool(max_workers) as pool:
            return pool.map(binary_search_wrapper, [(lst1, x) for x in lst2])

class TestMapBinarySearch(unittest.TestCase):
    def test_map_binary_search(self):
        lst1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        lst2 = [5, 10, 1]
        self.assertListEqual(map_binary_search(lst1, lst2, 2), [True, True, True])

        lst3 = [1, 2, 3, 4, 6, 7, 8, 9, 10]
        lst4 = [5, 11, 0]
        self.assertListEqual(map_binary_search(lst3, lst4, 2), [False, False, False])

        lst5 = []
        lst6 = [5, 11, 0]
        self.assertListEqual(map_binary_search(lst5, lst6, 2), [False, False, False])
        
        lst7 = [5]
        lst8 = [5, 10, 1]
        self.assertListEqual(map_binary_search(lst7, lst8, 2), [True, False, False])
        
if __name__ == '__main__':
    unittest.main()