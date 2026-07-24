from abc import ABC, abstractmethod
from dotenv import load_dotenv
import os
import importlib
from sorter import Sorter
load_dotenv()  # Load environment variables from .env file



# Define names as strings
module_name = os.getenv("module_name", "utils")  # Default to "utils" if not set
class_name = os.getenv("class_name", "MergeSort")  # Default to "MergeSort" if not set

# 1. Dynamically import the module
module = importlib.import_module(module_name)

# 2. Extract the class from the module
DynamicClass = getattr(module, class_name)

# 3. Use the class normally
user_instance = DynamicClass()
print(user_instance.sort([3, 1, 2]))  # Output: [1, 2, 3]



class QuickSort(Sorter):
    def sort(self, data):
        if len(data) <= 1:
            return data
        pivot = data[len(data) // 2]
        left = [x for x in data if x < pivot]
        middle = [x for x in data if x == pivot]
        right = [x for x in data if x > pivot]
        return self.sort(left) + middle + self.sort(right)

class BubbleSort(Sorter):
    def sort(self, data):
        n = len(data)
        for i in range(n):
            for j in range(0, n-i-1):
                if data[j] > data[j+1]:
                    data[j], data[j+1] = data[j+1], data[j]
        return data

class BinarySearch:
    def search(self, data, target):
        left, right = 0, len(data) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if data[mid] == target:
                return mid
            elif data[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1

class DependencyInjection:
    def __init__(self, sorter: Sorter):
        self.sorter = sorter

    def sort_data(self, data):
        return self.sorter.sort(data)

def resolve_sort_algorithm(sort_algo: str):
    if not sort_algo:
        raise ValueError("SORT_ALGORITHM is not set")

    # Backward compatible: class name declared in this module
    if sort_algo in globals():
        return globals()[sort_algo]

    # Support fully-qualified path, e.g. utils.mergesort.MergeSort
    if "." in sort_algo:
        module_path, class_name = sort_algo.rsplit(".", 1)
        module = importlib.import_module(module_path)
        return getattr(module, class_name)

    raise KeyError(sort_algo)

def main():
    print("Hello, Dependency Injection!")  
    # sort
    # loosely coupled sorting algorithm
    # Depends on the injected sorter (QuickSort or BubbleSort)
    sortAlgo = os.getenv("SORT_ALGORITHM")  # Get the sorting algorithm from environment variable
    print(f"Using sorting algorithm: {sortAlgo}")
    sorter_class = resolve_sort_algorithm(sortAlgo)
    di = DependencyInjection(sorter_class())
    data = [64, 34, 25, 12, 22, 11, 90]
    print("Original data:", data)
    sorted_data = di.sort_data(data)
    print("Sorted data:", sorted_data)

    #sorter = QuickSort()
    # Binary search 
    searcher = BinarySearch()
    target = 22
    index = searcher.search(sorted_data, target)
    if index != -1:
        print(f"Element {target} found at index {index}")
    else:
        print(f"Element {target} not found in the list")

if __name__ == "__main__":
    main()