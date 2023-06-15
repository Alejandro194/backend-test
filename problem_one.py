import unittest

"""
Escribe una función llamada merge_arrays que acepte dos arrays ordenados de enteros como parámetros
y devuelva un solo array ordenado que contenga todos los elementos de ambos.
"""


def merge_arrays(arr1, arr2):
    if len(arr1) == 0:
        return arr2
    elif len(arr2) == 0:
        return arr1
    merged = []
    i, j = 0, 0
    if is_order_ascend(arr1) and is_order_ascend(arr2):
        while i < len(arr1) and j < len(arr2):
            if arr1[i] < arr2[j]:
                merged.append(arr1[i])
                i += 1
            else:
                merged.append(arr2[j])
                j += 1
        merged += arr1[i:]
        merged += arr2[j:]
    elif not is_order_ascend(arr1) and not is_order_ascend(arr2):
        while i < len(arr1) and j < len(arr2):
            if arr1[i] > arr2[j]:
                merged.append(arr1[i])
                i += 1
            else:
                merged.append(arr2[j])
                j += 1
        merged += arr1[i:]
        merged += arr2[j:]
    else:
        if is_order_ascend(arr1):
            j = len(arr2) - 1
            while i < len(arr1) and j >= 0:
                if arr1[i] < arr2[j]:
                    merged.append(arr1[i])
                    i += 1
                else:
                    merged.append(arr2[j])
                    j -= 1
            merged += arr1[i:]
            merged += arr2[:j+1][::-1]
        else:
            i = len(arr1) - 1
            while i >= 0 and j < len(arr2):
                if arr1[i] < arr2[j]:
                    merged.append(arr1[i])
                    i -= 1
                else:
                    merged.append(arr2[j])
                    j += 1
            merged += arr2[j:]
            merged += arr1[:i+1][::-1]
    return merged


def is_order_ascend(arr):
    if len(arr) == 1:
        return True
    elif arr[0] < arr[-1]:
        return True
    else:
        return False

class TestMergeArray(unittest.TestCase):
    def test_merge_arrays(self):
        arr1 = [-1,-3,-5,-7,-9]
        arr2 = [2,4,6,8,10]
        result = [-9,-7,-5,-3,-1,2,4,6,8,10]
        self.assertEqual(merge_arrays(arr1,arr2),result)
    
if __name__ == '__main__':
    unittest.main()