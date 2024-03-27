import time  # Importing the time module for time-related functions
import tkinter as tk  # Importing the tkinter module for GUI
from tkinter import messagebox  # Importing messagebox module from tkinter for displaying messages
from colorama import init, Fore, Style  # Importing colorama module for colored text

# Initialize colorama for cross-platform ANSI color support
init(autoreset=True)

# Global variable to hold the array
simarray1 = [42, 32, 23, 12, 19, 54]

# Create Tkinter window
root = tk.Tk()

# Set the title of the Tkinter window
root.title("Standard Algorithms Simulator")

# Function to convert an array into a string for printing
def print_array(arr):
    return "[" + " ".join(map(str, arr)) + "]"

# Function to perform bubble sort algorithm
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Swap elements if they are in the wrong order
                array_label.config(text=print_array(arr))  # Update array_label in GUI
                root.update()  # Update the GUI
                time.sleep(1)  # Pause for 1 second

# Function to perform binary search algorithm
def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return mid  # Return the index if the element is found
        elif arr[mid] < x:
            low = mid + 1  # Continue searching in the right half
        else:
            high = mid - 1  # Continue searching in the left half
    return -1  # Return -1 if the element is not found

# Function to perform bubble sort and display the sorted array in the GUI
def perform_bubble_sort():
    bubble_sorted_array = simarray1.copy()
    bubble_sort(bubble_sorted_array)
    sorted_array_label.config(text=print_array(bubble_sorted_array))

# Function to perform binary search and display the search result in a message box
def perform_binary_search():
    search_value = int(search_entry.get())
    bubble_sorted_array = sorted(simarray1)
    index = binary_search(bubble_sorted_array, search_value)
    if index != -1:
        messagebox.showinfo("Binary Search Result", f"Value {search_value} found at index {index}")
    else:
        messagebox.showwarning("Binary Search Result", f"Value {search_value} not found in the array")

# Function for bubble sort in command-line interface (CLI)
def cli_bubble_sort():
    bubble_sorted_array = simarray1.copy()
    bubble_sort(bubble_sorted_array)
    print("\nArray sorted using Bubble Sort:", bubble_sorted_array)

# Function for binary search in command-line interface (CLI)
def cli_binary_search():
    search_value = int(input("Enter the value to search for: "))
    bubble_sorted_array = sorted(simarray1)
    index = binary_search(bubble_sorted_array, search_value)
    if index != -1:
        print(Fore.GREEN + f"Value {search_value} found at index {index}")
    else:
        print(Fore.RED + f"Value {search_value} not found in the array")

# GUI Elements
array_label = tk.Label(root, text=print_array(simarray1))  # Label to display the array in the GUI
array_label.pack()  # Pack the array label into the window

bubble_sort_button = tk.Button(root, text="Bubble Sort", command=perform_bubble_sort)  # Button to trigger bubble sort
bubble_sort_button.pack()  # Pack the bubble sort button into the window

sorted_array_label = tk.Label(root, text="")  # Label to display the sorted array in the GUI
sorted_array_label.pack()  # Pack the sorted array label into the window

search_frame = tk.Frame(root)  # Frame to contain search-related elements
search_frame.pack()  # Pack the search frame into the window

search_label = tk.Label(search_frame, text="Enter value to search:")  # Label for the search entry
search_label.pack(side="left")  # Pack the search label into the search frame

search_entry = tk.Entry(search_frame)  # Entry widget to enter the search value
search_entry.pack(side="left")  # Pack the search entry into the search frame

binary_search_button = tk.Button(root, text="Binary Search", command=perform_binary_search)  # Button to trigger binary search
binary_search_button.pack()  # Pack the binary search button into the window

exit_button = tk.Button(root, text="Exit", command=root.destroy)  # Button to exit the program
exit_button.pack()  # Pack the exit button into the window

# Main function for command-line interface (CLI)
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
            cli_bubble_sort()

        elif choice == "2":
            print("\nBinary Search:")
            cli_binary_search()

        elif choice == "3":
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()

root.mainloop()  # Start the Tkinter event loop
