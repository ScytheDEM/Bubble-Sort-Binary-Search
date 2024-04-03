import time  # import the time module for pausing the program
from colorama import init, Fore, Style  # import the colorama module for ANSI color support

# initialize colorama for cross-platform ANSI color support
init(autoreset=True)

# global variable to hold the array
simarray1 = [42, 32, 23, 12, 19, 54] # define a list of integers

# function to print the elements of an array
def print_array(arr): # function to print the array
    print("[", end="") # print the opening bracket
    for i in range(len(arr)): # iterate over the array
        print(arr[i], end=" ") # print the element
    print("]") # print the closing bracket 

# function to perform bubble sort on an array
def bubble_sort(arr):   # function to perform bubble sort
    n = len(arr) # get the length of the array
    for i in range(n): # iterate over the array
        for j in range(0, n - i - 1): # iterate over the unsorted part of the array
            if arr[j] > arr[j + 1]:     # check if the current element is greater than the next element
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # swap the elements if they are in the wrong order
                print_array(arr)  # print the array after each swap
                time.sleep(1)  # pause for 1 second

# function to perform binary search on a sorted array
def binary_search(arr, x): # function to perform binary search
    low = 0 # initialize the lower bound
    high = len(arr) - 1 # initialize the upper bound
    while low <= high: # perform binary search until the lower bound is less than or equal to the upper bound
        mid = (low + high) // 2 # calculate the middle index
        if arr[mid] == x: # check if the middle element is equal to the search value
            return mid  # return the index if the value is found
        elif arr[mid] < x: # if the middle element is less than the search value
            low = mid + 1  # update the lower bound
        else: # if the middle element is greater than the search value
            high = mid - 1  # update the upper bound
    return -1  # return -1 if the value is not found

# main function
def main(): # main function
    print("welcome to the bubble sort - binary search program") # welcome message
    while True: # run the program in a loop
        print("\nMain Menu:") # print the main menu
        print("1. bubble sort") # print the options
        print("2. binary search") # print the options
        print("3. exit the program (quit)")     # print the options
        choice = input("select your choice with the keyboard numbers: ") # get the user's choice

        if choice == "1":   # if the user chooses option 1
            print("\nbubble sort:") # print the bubble sort message
            bubble_sorted_array = simarray1.copy()  # create a copy of the array
            bubble_sort(bubble_sorted_array)  # sort the array using bubble sort
            print("\narray is sorted using bubble sort:", bubble_sorted_array) # print the sorted array

        elif choice == "2": # if the user chooses option 2
            print("\nbinary search:") # print the binary search message
            search_value = int(input("enter the value to search for!: "))
            bubble_sorted_array = sorted(simarray1)  # sort the array
            print("Sorted Array:", bubble_sorted_array) # print the sorted array
            index = binary_search(bubble_sorted_array, search_value)  # perform binary search
            if index != -1: # if the value is found
                print(Fore.GREEN + f"value {search_value} found at index {index}")  # print success message
            else: # if the value is not found
                print(Fore.RED + f"value {search_value} is not found in the array :(")  # print failure message

        elif choice == "3": # if the user chooses option 3
            print("now closing the program, until next time! :)") # print the closing message
            break # break the loop to exit the program

        else: # if the user enters an invalid choice
            print("invalid. please enter a valid choice") # print an error message

# run the main function if the script is executed directly
if __name__ == "__main__": # if the script is executed directly
    main() # run the main function
