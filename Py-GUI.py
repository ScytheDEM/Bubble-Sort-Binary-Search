#!/usr/bin/env python3
import time  # Import the time module for adding delays
import tkinter as tk  # Import the tkinter module for GUI
from tkinter import messagebox  # Import the messagebox module from tkinter
# stuff above is needed for the import of data to the computer

simarray1 = [42, 32, 23, 12, 19, 54]  # Define a list of integers

root = tk.Tk()  # Create a tkinter root window
root.title("Standard Algorithms Simulator")  # Set the title of the root window

def print_array(arr):
    return "[" + " ".join(map(str, arr)) + "]"  # Convert the array to a string representation

def bubble_sort(arr):
    n = len(arr)  # Get the length of the array (n represents the length of the array)
    for i in range(n):  # Iterate over the array (i represents as the counter for the outerloop that iterates through the array mukltiple times to sort the array)
        is_sorted = True  # Flag to check if the array is already sorted
        for j in range(0, n - i - 1):  # Iterate over the unsorted part of the array (j serves as a counter for the inner loop which is the sorting a position of the array in each pass as it slowly shrinks as less needs to be sorted. )
            if arr[j] > arr[j + 1]:  # If the current element is greater than the next element
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Swap the elements
                is_sorted = False  # Set the flag to False
                array_label.config(text=print_array(arr))  # Update the label with the sorted array
                root.update()  # Update the GUI
                time.sleep(0.5)  # Add a delay to visualize the sorting process
        if is_sorted:  # If the array is already sorted, break the loop
            break
    return arr  # Return the sorted array

def binary_search(arr, x, low, high):
    while low <= high:  # Perform binary search until the low index is less than or equal to the high index
        mid = (low + high) // 2  # Calculate the middle index
        if arr[mid] == x:  # If the middle element is equal to the search value
            return mid  # Return the index of the middle element
        elif arr[mid] < x:  # If the middle element is less than the search value
            low = mid + 1  # Update the low index to search in the right half of the array
        else:  # If the middle element is greater than the search value
            high = mid - 1  # Update the high index to search in the left half of the array
    return -1  # Return -1 if the search value is not found in the array

def perform_bubble_sort():
    bubble_sort(simarray1)  # Call the bubble_sort function to sort the array
    sorted_array_label.config(text=print_array(simarray1))  # Update the label with the sorted array

def perform_binary_search():
    if not sorted_array_label.cget("text"):  # If the sorted array label is empty
        messagebox.showerror("Error", "Please run Bubble Sort first to sort the array.")  # Show an error message
        return

    search_value = search_entry.get().strip()  # Get the search value from the entry widget and remove leading/trailing spaces
    if not search_value:  # If the search value is empty
        messagebox.showerror("Error", "Please enter a value to search.")  # Show an error message
        return

    try:
        search_value = int(search_value)  # Convert the search value to an integer
    except ValueError:  # If the search value is not a valid integer
        messagebox.showerror("Error", "Please enter a valid integer.")  # Show an error message
        return

    index = binary_search(simarray1, search_value, 0, len(simarray1) - 1)  # Call the binary_search function to search for the value
    if index != -1:  # If the value is found in the array
        messagebox.showinfo("Binary Search Result", f"Value {search_value} found at index {index}")  # Show an info message
    else:  # If the value is not found in the array
        messagebox.showwarning("Binary Search Result", f"Value {search_value} not found in the array")  # Show a warning message
        # im so proud of the animations within the code and the sorting process. 
        # NOTE SOME OF THE BUTTONS MIGHT BE A BIT LAGGY, BLAME PYTHON NOT ME, LIVE LAUGH LOVE APPLE SILICON!!!!!!

def show_main_screen():
    homescreen_frame.pack_forget()  # Hide the homescreen frame
    main_frame.pack()  # Show the main frame

def show_homescreen():
    main_frame.pack_forget()  # Hide the main frame
    homescreen_frame.pack()  # Show the homescreen frame
# Below is the code for the GUI, which includes the homescreen, main screen, and the functionality to perform bubble sort and binary search on an array. The GUI is created using the tkinter library in Python. 
    # the gui is completly seperate and doesn't need to be included for the code above to work, a layer of CMI code might be needed, can be found on the added page in the github


homescreen_frame = tk.Frame(root)  # Create a frame for the homescreen
homescreen_frame.pack()  # Pack the homescreen frame

homescreen_label = tk.Label(homescreen_frame, text="Welcome to Standard Algorithms Simulator")  # Create a label for the homescreen
homescreen_label.pack()  # Pack the homescreen label

begin_button = tk.Button(homescreen_frame, text="Begin", command=show_main_screen)  # Create a button to begin the simulation
begin_button.pack()  # Pack the begin button

main_frame = tk.Frame(root)  # Create a frame for the main screen

back_button = tk.Button(main_frame, text="Back", command=show_homescreen)  # Create a button to go back to the homescreen
back_button.pack()  # Pack the back button

array_label = tk.Label(main_frame, text=print_array(simarray1))  # Create a label to display the array
array_label.pack()  # Pack the array label

bubble_sort_button = tk.Button(main_frame, text="Bubble Sort", command=perform_bubble_sort)  # Create a button to perform bubble sort
bubble_sort_button.pack()  # Pack the bubble sort button

sorted_array_label = tk.Label(main_frame, text="")  # Create a label to display the sorted array
sorted_array_label.pack()  # Pack the sorted array label

search_frame = tk.Frame(main_frame)  # Create a frame for the search functionality
search_frame.pack()  # Pack the search frame

search_label = tk.Label(search_frame, text="Enter value to search:")  # Create a label for the search entry
search_label.pack(side="left")  # Pack the search label to the left

search_entry = tk.Entry(search_frame)  # Create an entry widget for the search value
search_entry.pack(side="left")  # Pack the search entry to the left

binary_search_button = tk.Button(main_frame, text="Binary Search", command=perform_binary_search)  # Create a button to perform binary search
binary_search_button.pack()  # Pack the binary search button

exit_button = tk.Button(main_frame, text="Exit", command=root.destroy)  # Create a button to exit the program
exit_button.pack()  # Pack the exit button

def main():
    show_homescreen()  # Show the homescreen
    root.mainloop()  # Start the tkinter event loop

if __name__ == "__main__":
    main()  # Call the main function to start the program
