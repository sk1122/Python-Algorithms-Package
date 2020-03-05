from main import Search, Sort


arr = [10, 20, 40, 30, 50]
arr1 = [10, 40, 20, 50, 30]
n = 40

s = Search()
print("\tSearching..\n")
print(f"Linear Search: {s.linear_search(arr, n)}")
print(f"Binary Search: {s.binary_search(arr, 0, len(arr)-1, n)}")

print("\n\n")

s1 = Sort()
print("\tSorting..\n")
print(f"Bubble Sort: {s1.bubble_sort(arr1)}")
print(f"Selection Sort: {s1.selection_sort(arr1)}")
print(f"Insertion Sort: {s1.insertion_sort(arr1)}")
print(f"Merge Sort: {s1.merge_sort(arr1)}")
