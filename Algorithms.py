"""
    Author : Satyam Kulkarni
    Version : 1.0.0
    Python Package

    https://github.com/sk1122/Alogrithm-Package-Python
    https://pypi.org
"""

class Search:
    """
        class Search

        :params = arr - list of elements (sorted)
        :params = n - key
    """


    def linear_search(self, arr, n):
        for i in range(len(arr)):
            if arr[i] == n:
                return i
        return -1

    def binary_search(self, arr, start, end, n):
        mid = (start + end) // 2

        if arr[mid] == n:
            return mid
        elif arr[mid] < n:
            return binarySearch(arr, mid + 1, end, n)
        elif arr[mid] > n:
            return binarySearch(arr, 0, start-1, n)
        else:
            return -1

class Sort:
    def bubble_sort(self, arr):
        """
        Function Binary Sort

        :params = arr - list of elements
        """

        for i in range(len(arr)-1):
            for j in range(i, len(arr)):
                if arr[i] > arr[j]:
                    arr[i], arr[j] = arr[j], arr[i]
        return arr

    def selection_sort(self, arr):
        """
        Function Selection Sort

        :params = arr - list of elements
        """

        for i in range(len(arr)):
            min_idx = i
            for j in range(i+1, len(arr)):
                if arr[j] > arr[min_idx]:
                    min_idx = j

            arr[i], arr[min_idx] = arr[min_idx], arr[i]
        a = list(reversed(arr))
        return a

    def insertion_sort(self, arr):
        for i in range(len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and key < arr[j]:
                arr[j+1] = arr[j]
                j -= 1
            arr[j+1] = key

        return arr

    def merge_sort(self, arr):
        if len(arr) > 1:
            mid = len(arr) // 2
            L = arr[:mid]
            R = arr[mid:]

            Sort.merge_sort(self, L)
            Sort.merge_sort(self, R)

            i = j = k = 0

            while i < len(L) and j < len(R):
                if L[i] < R[j]:
                    arr[k] = L[i]
                    i += 1
                else:
                    arr[k] = R[j]
                    j += 1
                k += 1

            while i < len(L):
                arr[k] = L[i]
                i += 1
                k += 1

            while j < len(R):
                arr[k] = R[j]
                j += 1
                k += 1

            return arr
