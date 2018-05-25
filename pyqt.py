import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        super().__init__() # Initialize the parent class.
        # Create layout
        grid = QGridLayout()
        self.setLayout(grid)
        self.setGeometry(10, 10, 300, 500) # topleftx, toplefty, width, height (pixels)

        # Create widgets
        label = QLabel("Hello, world", self) # Create label for the window
        grid.addWidget(label, 1, 1, 1, 1) # row, col, span_row, span_col

        label2 = QLabel("I don't know", self)
        grid.addWidget(label2, 2, 1, 1, 2)
        label2.setAlignment(Qt.AlignCenter)

        label3 = QLabel("Label 3", self)
        grid.addWidget(label3, 1, 2, 1, 1)

        btn1 = QPushButton("Push me", self)
        grid.addWidget(btn1, 3, 1,  1, 1)

        label_btn1 = QLabel("Not pushed", self)
        grid.addWidget(label_btn1, 3, 2, 1, 1)

        # Slots and signals
        # Signals are sent when an event occurs.
        # A slot is a place for the signal to go
        btn1.clicked.connect(lambda: label_btn1.setText("Pushed"))

        # Draw gui
        self.show()

if __name__ == "__main__":
    '''main program goes here'''
    app = QApplication(sys.argv)
    gui = Window() # Graphical user interface
    sys.exit(app.exec())

# make calculator
# eval