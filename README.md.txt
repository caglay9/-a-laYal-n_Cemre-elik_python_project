Function Plotter Project

Description
This project is a Python-based graphical application for plotting mathematical functions. Built using PyQt5, Matplotlib, and NumPy, the program provides users with an interactive interface to visualize and customize mathematical functions in real-time. The application allows users to input a function, customize its appearance, and plot it within a specified range.

Features
1. Interactive Input: Users can input any valid mathematical function of x (e.g., x**2, np.sin(x), etc.).
2. Customizable Appearance:
   - Select line color (e.g., blue, red, green, etc.).
   - Choose line style (e.g., solid, dashed, dotted, etc.).
   - Toggle grid visibility.
3. Error Handling: Provides feedback for invalid or empty inputs with error messages.
4. Real-Time Plotting: Displays the graph of the entered function in real time with the option to update or modify settings.
5. The Interface: Built with PyQt5 for a user-friendly graphical interface.

Technologies Used
- Python: Core programming language.
- PyQt5: For creating the graphical user interface (GUI).
- Matplotlib: For plotting mathematical functions.
- NumPy: For numerical computation and function evaluation.

Installation and Setup
Prerequisites
Ensure you have the following installed on the system:
1. Python 
2. pip 

Installing Dependencies
Run the following command to install required Python libraries:
pip install PyQt5 matplotlib numpy


Running the Program
1. Download the advanced_function_plotter.py file.
2. Open a terminal or command prompt.
3. Navigate to the directory where the file is located.
4. Run the program using Python
5. The application window will open, allowing you to input functions and plot them.

How to Use
1. Enter a valid mathematical function of x in the input field (e.g., x**2, np.sin(x)).
2. Customize the appearance of the plot:
   - Choose the line color from the dropdown menu.
   - Select the line style (solid, dashed, dotted, etc.).
   - Toggle the grid on or off using the checkbox.
3. Click the "Plot Function" button to generate the plot.
4. If the input function is invalid, an error message will appear, guiding you to correct it.

Example Functions
There are some examples of functions you can plot:
- x**2 (Parabola)
- np.sin(x) (Sine wave)
- np.exp(x) (Exponential function)
- np.sin(x) * np.exp(-0.1*x) (Damped sine wave)



Limitations
1. The function input must be in Python syntax.
2. Only one function can be plotted at a time.
3. The function must be expressed in terms of x and should use NumPy for advanced operations (e.g., np.sin(x), np.exp(x)).
