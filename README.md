# Bubble-Sort-Binary-Search

<img width="849" alt="Screenshot 2024-04-03 at 6 48 01 pm" src="https://github.com/ScytheDEM/Bubble-Sort-Binary-Search/assets/89125983/3b4bf2bd-27dc-4dcd-b803-bba55e928550">


# Standard Algorithms Simulator


This repository contains a Standard Algorithms Simulator developed as part of my School Of Now Assessment task 2. The program includes modules for implementing two fundamental algorithms: Bubble Sort and Binary Search. 
- Includes bidirectional navigation and a main menu for ease of use.


## Task Description

As per the client's brief, the task involves developing a Modular Approach to software development, focusing on separating a program's functions into independent pieces or building blocks. 
Specifically, this task requires the development of a Standard Algorithms Simulator incorporating the following algorithms:

1. Bubble Sort
2. Binary Search

The simulator should includes bidirectional navigation and a main menu for smooth user interaction.

## Algorithm Description

### Bubble Sort
Bubble Sort is a simple sorting algorithm that repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order. The pass through the list is repeated until the list is sorted.

### Binary Search
Binary Search is a search algorithm that finds the position of a target value within a sorted array. It compares the target value to the middle element of the array and continues narrowing down the search by halving the search interval in each step.

## Code Overview

The provided code implements the Standard Algorithms Simulator:

- `print_array(arr)`: Function to print the elements of an array.
- `bubble_sort(arr)`: Function to perform bubble sort on an array.
- `binary_search(arr, x)`: Function to perform binary search on a sorted array.
- `main()`: Main function containing the menu and user interface logic.

## Usage

# To run the simulator:
(You are required to have an IDE program for debugging purposes, Visual Studio is a good, free application: https://code.visualstudio.com/)
1. Execute the Python script.
  - Download the Python CLI Visual Code plugin
    https://marketplace.visualstudio.com/items?itemName=ms-python.python
  - Download the Python application for your computer platform
    Windows: https://www.python.org/downloads/windows/
    Mac: https://www.python.org/downloads/macos/
    Linux: https://www.python.org/downloads/source/

2. Open the file using Visual Studio Code, go to 'run' on the top bar (if on a Mac) and select 'start debugging'

If on a windows device, click the 'F5' key. 

3. Debug Config: 

Since you already installed the 'debugger' on the visual studio marketplace, click 'python file' when the drop down at the top-middle of the screen comes down (as showed below) 

<img width="628" alt="Screenshot 2024-04-03 at 6 55 44 pm" src="https://github.com/ScytheDEM/Bubble-Sort-Binary-Search/assets/89125983/643fee39-b17c-448e-8867-3e1918a02503">

The application should now load!

(NOTE: THE DEBUGGER IS RECOMMENDED FOR NORMAL USERS AS IT CAN IDENTIFY ERRORS, PLEASE LEAVE A 'ISSUE' IN THE 'ISSUES' TAB SO I CAN ASSIST!



# To run the app WITHOUT using an IDE program:

1. Download a copy of the latest version of python at https://www.python.org/downloads/ .

2. Download the file, right click on the file

3. (FOR MAC) If on a Mac, Hold down the 'option key', go to 'Open always with' and select 'pythonlauncher.app'

(FOR WINDOWS) If on a windows device, right click the file, go to 'open' and select 'python / python launcher'

The application should now load in a small window. The window is resizable to any size desired. 


## Internal Documentation

The code includes comments explaining implemented modules, variables & structures.

Please note, the 'GUI' is a wrapper for the actual searching program. This is done by design for people to change the UI or adapt the code into different applications. The GUI has no function except for clickable functions. 

## Files Included

- `standard_algorithms_simulator.py`: Python script containing the implementation of the Standard Algorithms Simulator.

## Requirements

The code requires Python 3.x and the `colorama` module for ANSI color support.

## Credits

All programming is credited to Alic Lonsdale - School Of Now, this code is although open for anyone to make modifications to. Please contact me on aliclonsdale@gmail.com to tell me first !
