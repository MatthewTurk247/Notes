import sys
from math import sqrt
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class Window(QWidget):
    def __init__(self):
        super().__init__()

        # Layout
        self.grid = QGridLayout()
        self.setLayout(self.grid)
        self.setGeometry(10, 10, 100, 300)

        # Widgets
        self.answer = QLabel("")
        self.answer.setObjectName('answer')
        self.grid.addWidget(self.answer, 1, 1, 1, 4)

        self.button1 = QPushButton("1")
        self.grid.addWidget(self.button1, 5, 1, 1, 1)

        self.button2 = QPushButton("2")
        self.grid.addWidget(self.button2, 5, 2, 1, 1)

        self.button3 = QPushButton("3")
        self.grid.addWidget(self.button3, 5, 3, 1, 1)

        self.button4 = QPushButton("4")
        self.grid.addWidget(self.button4, 4, 1, 1, 1)

        self.button5 = QPushButton("5")
        self.grid.addWidget(self.button5, 4, 2, 1, 1)

        self.button6 = QPushButton("6")
        self.grid.addWidget(self.button6, 4, 3, 1, 1)

        self.button7 = QPushButton("7")
        self.grid.addWidget(self.button7, 3, 1, 1, 1)

        self.button8 = QPushButton("8")
        self.grid.addWidget(self.button8, 3, 2, 1, 1)

        self.button9 = QPushButton("9")
        self.grid.addWidget(self.button9, 3, 3, 1, 1)

        self.button0 = QPushButton("0")
        self.grid.addWidget(self.button0, 6, 1, 1, 2)

        self.button_add = QPushButton("+")
        self.grid.addWidget(self.button_add, 5, 4, 1, 1)

        self.button_multiply = QPushButton("x")
        self.grid.addWidget(self.button_multiply, 3, 4, 1, 1)
        # school progject
        # programming
        # the website

        # QWidget background color rgba(200, 200, 200, 0.5)

        self.button_divide = QPushButton("÷")
        self.grid.addWidget(self.button_divide, 2, 4, 1, 1)

        self.button_subtract = QPushButton("-")
        self.grid.addWidget(self.button_subtract, 4, 4, 1, 1)

        self.button_clear = QPushButton("C")
        self.grid.addWidget(self.button_clear, 2, 1, 1, 2)

        self.button_sqrt = QPushButton("√")
        self.grid.addWidget(self.button_sqrt, 2, 3, 1, 1)
        # inital salary is extremely important because it compounds
        # hire someone to negotiate

        self.button_point = QPushButton(".")
        self.grid.addWidget(self.button_point, 6, 3, 1, 1)

        self.calc_button = QPushButton("=")
        self.grid.addWidget(self.calc_button, 6, 4, 1, 1)

        # Signals and Slots
        self.button1.clicked.connect(lambda: self.answer.setText(self.answer.text() + "1"))
        self.button2.clicked.connect(lambda: self.answer.setText(self.answer.text() + "2"))
        self.button3.clicked.connect(lambda: self.answer.setText(self.answer.text() + "3"))
        self.button4.clicked.connect(lambda: self.answer.setText(self.answer.text() + "4"))
        self.button5.clicked.connect(lambda: self.answer.setText(self.answer.text() + "5"))
        self.button6.clicked.connect(lambda: self.answer.setText(self.answer.text() + "6"))
        self.button7.clicked.connect(lambda: self.answer.setText(self.answer.text() + "7"))
        self.button8.clicked.connect(lambda: self.answer.setText(self.answer.text() + "8"))
        self.button9.clicked.connect(lambda: self.answer.setText(self.answer.text() + "9"))
        self.button0.clicked.connect(lambda: self.answer.setText(self.answer.text() + "0"))

        self.button_sqrt.clicked.connect(lambda: self.answer.setText(str(sqrt(float(self.answer.text())))))
        self.button_multiply.clicked.connect(lambda: self.answer.setText(self.answer.text() + "*"))
        self.button_divide.clicked.connect(lambda: self.answer.setText(self.answer.text() + "/"))
        self.button_subtract.clicked.connect(lambda: self.answer.setText(self.answer.text() + " - "))
        self.button_clear.clicked.connect(lambda: self.answer.setText(""))
        self.button_add.clicked.connect(lambda: self.answer.setText(self.answer.text() + " + "))
        self.button_point.clicked.connect(lambda: self.answer.setText(self.answer.text() + "."))
        try:
            self.calc_button.clicked.connect(self.evaluate_expression)
        except ZeroDivisionError:
            self.answer.setText("Error")

        # Style
        self.set_style()

        # Draw
        self.show()

    def set_style(self):
        style_sheet = 'calc_style.css'
        with open(style_sheet, 'r') as f:
            self.setStyleSheet(f.read())

    def evaluate_expression(self):
        self.answer.setText(str(eval(self.answer.text())))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    gui = Window()
    sys.exit(app.exec())