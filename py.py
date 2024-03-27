import time  # import the time module for pausing the program
from colorama import init, Fore, Style  # import the colorama module for ANSI color support

# initialize colorama for cross-platform ANSI color support
init(autoreset=True)

# global variable to hold the array
simarray1 = [42, 32, 23, 12, 19, 54]

# function to print the elements of an array
def print_array(arr):
    print("[", end="")
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print("]")

# function to perform bubble sort on an array
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # swap the elements if they are in the wrong order
                print_array(arr)  # print the array after each swap
                time.sleep(1)  # pause for 1 second

# function to perform binary search on a sorted array
def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return mid  # return the index if the value is found
        elif arr[mid] < x:
            low = mid + 1  # update the lower bound
        else:
            high = mid - 1  # update the upper bound
    return -1  # return -1 if the value is not found

# main function
def main():
    print("Welcome to Standard Algorithms Simulator")
    while True:
        print("\nMain Menu:")
        print("1. Bubble Sort")
        print("2. Binary Search")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            print("\nBubble Sort:")
            bubble_sorted_array = simarray1.copy()  # create a copy of the array
            bubble_sort(bubble_sorted_array)  # sort the array using bubble sort
            print("\nArray sorted using Bubble Sort:", bubble_sorted_array)

        elif choice == "2":
            print("\nBinary Search:")
            search_value = int(input("Enter the value to search for: "))
            bubble_sorted_array = sorted(simarray1)  # sort the array
            print("Sorted Array:", bubble_sorted_array)
            index = binary_search(bubble_sorted_array, search_value)  # perform binary search
            if index != -1:
                print(Fore.GREEN + f"value {search_value} found at index {index}")  # print success message
            else:
                print(Fore.RED + f"value {search_value} not found in the array")  # print failure message

        elif choice == "3":
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a valid option.")

# run the main function if the script is executed directly
if __name__ == "__main__":
    main()
