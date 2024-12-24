
import sys
import numpy as np
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import (QApplication, QMainWindow, QVBoxLayout, QLineEdit, QPushButton, QWidget, QLabel, QMessageBox, QHBoxLayout, QCheckBox, QComboBox)
from matplotlib.backends.backend_qt5agg import (FigureCanvasQTAgg as FigureCanvas, NavigationToolbar2QT as NavigationToolbar)

class FunctionPlotter(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Advanced Function Plotter")
        self.setGeometry(100, 100, 900, 700)

        # Main widget and layout
        self.main_widget = QWidget()
        self.setCentralWidget(self.main_widget)
        self.layout = QVBoxLayout(self.main_widget)

        # Input field for function
        self.function_label = QLabel("Enter a function (in terms of x):")
        self.layout.addWidget(self.function_label)

        self.function_input = QLineEdit()
        self.layout.addWidget(self.function_input)

        # Additional options layout
        self.options_layout = QHBoxLayout()

        # Checkbox for grid
        self.grid_checkbox = QCheckBox("Show Grid")
        self.grid_checkbox.setChecked(True)
        self.options_layout.addWidget(self.grid_checkbox)

        # Dropdown for color
        self.color_label = QLabel("Line Color:")
        self.options_layout.addWidget(self.color_label)
        self.color_dropdown = QComboBox()
        self.color_dropdown.addItems(["blue", "red", "green", "black", "purple"])
        self.options_layout.addWidget(self.color_dropdown)

        # Dropdown for line style
        self.style_label = QLabel("Line Style:")
        self.options_layout.addWidget(self.style_label)
        self.style_dropdown = QComboBox()
        self.style_dropdown.addItems(["-", "--", "-.", ":"])
        self.options_layout.addWidget(self.style_dropdown)

        self.layout.addLayout(self.options_layout)

        # Plot button
        self.plot_button = QPushButton("Plot Function")
        self.plot_button.clicked.connect(self.plot_function)
        self.layout.addWidget(self.plot_button)

        # Matplotlib canvas
        self.figure, self.ax = plt.subplots()
        self.canvas = FigureCanvas(self.figure)
        self.layout.addWidget(self.canvas)

        # Navigation toolbar
        self.toolbar = NavigationToolbar(self.canvas, self)
        self.layout.addWidget(self.toolbar)

    def plot_function(self):
        # Get the function input
        func_text = self.function_input.text()
        if not func_text:
            QMessageBox.warning(self, "Input Error", "Please enter a function.")
            return

        try:
            # Create a range of x values
            x = np.linspace(-10, 10, 1000)

            # Evaluate the function safely
            y = eval(func_text, {"x": x, "np": np})

            # Clear the axes and plot the new function
            self.ax.clear()

            # Apply user-selected styles
            color = self.color_dropdown.currentText()
            style = self.style_dropdown.currentText()
            self.ax.plot(x, y, color=color, linestyle=style, label=f"y = {func_text}")

            # Add grid if selected
            if self.grid_checkbox.isChecked():
                self.ax.grid(True)

            self.ax.set_title("Function Plot")
            self.ax.set_xlabel("x")
            self.ax.set_ylabel("y")
            self.ax.legend()

            # Redraw the canvas
            self.canvas.draw()

        except Exception as e:
            QMessageBox.critical(self, "Error", f"Invalid function or input: {e}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = FunctionPlotter()
    main_window.show()
    sys.exit(app.exec_())
