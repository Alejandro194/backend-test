'''
Escribe una función llamada find_median que acepte un array de enteros como parámetro y 
devuelva la mediana del conjunto.
'''

import unittest

def find_median(arr):
    n = len(arr)
    arr_sorted = sorted(arr)
    if n % 2 == 0:
        return (arr_sorted[n//2-1] + arr_sorted[n//2]) / 2
    else:
        return arr_sorted[n//2]
    
class TestFindMedian(unittest.TestCase):
    def test_find_median(self):
        arr = [1,2,3,4,5]
        result = 3
        self.assertEqual(find_median(arr),result)
    
if __name__ == '__main__':
    unittest.main()
