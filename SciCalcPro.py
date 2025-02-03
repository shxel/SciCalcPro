import sys
import math
from simpleeval import simple_eval, NameNotDefined, FunctionNotDefined
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QGridLayout, QPushButton,
    QLineEdit, QLabel, QTabWidget, QTextEdit, QAction, QMenuBar, QMessageBox
)
from PyQt5.QtGui import QFont, QKeyEvent
from PyQt5.QtCore import Qt, QDateTime


class CalculatorApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Advanced Calculator")
        self.setGeometry(100, 100, 450, 700)
        self.memory = 0
        self.history = []
        self.angle_mode = 'rad'  # 'rad' or 'deg'
        self.init_ui()

    def init_ui(self):
        # Main Layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        # Menu Bar
        self.create_menu()

        # Display Area
        self.display = QLineEdit(self)
        self.display.setFont(QFont("Arial", 18))
        self.display.setAlignment(Qt.AlignRight)
        self.display.setReadOnly(False)
        self.layout.addWidget(self.display)

        # Mode Tabs
        self.tabs = QTabWidget()
        self.standard_mode = QWidget()
        self.engineering_mode = QWidget()
        self.tabs.addTab(self.standard_mode, "Standard")
        self.tabs.addTab(self.engineering_mode, "Engineering")
        self.layout.addWidget(self.tabs)

        # Initialize Modes
        self.init_standard_mode()
        self.init_engineering_mode()

        # History Panel
        self.history_panel = QTextEdit(self)
        self.history_panel.setReadOnly(True)
        self.history_panel.setFont(QFont("Arial", 10))
        self.layout.addWidget(QLabel("History"))
        self.layout.addWidget(self.history_panel)

    def create_menu(self):
        menubar = self.menuBar()
        # Theme Menu
        theme_menu = menubar.addMenu("Theme")
        light_theme = QAction("Light Theme", self)
        dark_theme = QAction("Dark Theme", self)
        light_theme.triggered.connect(self.set_light_theme)
        dark_theme.triggered.connect(self.set_dark_theme)
        theme_menu.addAction(light_theme)
        theme_menu.addAction(dark_theme)
        # History Menu
        history_menu = menubar.addMenu("History")
        clear_history = QAction("Clear History", self)
        clear_history.triggered.connect(self.clear_history)
        history_menu.addAction(clear_history)

    def set_light_theme(self):
        self.setStyleSheet("""
            background-color: white;
            color: black;
            QPushButton {
                background-color: #f0f0f0;
                border: 1px solid #ccc;
                padding: 8px;
                font-size: 14px;
            }
            QPushButton:hover { background-color: #e0e0e0; }
            QLineEdit { background-color: white; border: 2px solid #ccc; }
        """)

    def set_dark_theme(self):
        self.setStyleSheet("""
            background-color: #2b2b2b;
            color: white;
            QPushButton {
                background-color: #404040;
                border: 1px solid #555;
                padding: 8px;
                font-size: 14px;
            }
            QPushButton:hover { background-color: #505050; }
            QLineEdit { background-color: #404040; border: 2px solid #555; }
        """)

    def init_standard_mode(self):
        layout = QVBoxLayout()
        buttons = [
            "MC", "MR", "M+", "M-",
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "0", ".", "=", "+",
            "C", "⌫"
        ]
        grid = self.create_button_grid(buttons, self.handle_standard_input)
        layout.addLayout(grid)
        self.standard_mode.setLayout(layout)

    def init_engineering_mode(self):
        layout = QVBoxLayout()
        buttons = [
            "sin", "cos", "tan", "log",
            "asin", "acos", "atan", "ln",
            "sqrt", "^", "!", "π",
            "e", "(", ")", "Deg/Rad",
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "0", ".", "=", "+",
            "C", "⌫"
        ]
        grid = self.create_button_grid(buttons, self.handle_engineering_input)
        layout.addLayout(grid)
        self.engineering_mode.setLayout(layout)

    def create_button_grid(self, buttons, handler):
        grid = QGridLayout()
        for i, text in enumerate(buttons):
            btn = QPushButton(text)
            btn.clicked.connect(lambda _, t=text: handler(t))
            if text in ["=", "⌫", "C"]:
                btn.setStyleSheet("background-color: #ff9933;")
            row, col = divmod(i, 4)
            grid.addWidget(btn, row, col)
        return grid

    def handle_standard_input(self, text):
        if text == "=":
            self.calculate_result()
        elif text == "C":
            self.display.clear()
        elif text == "⌫":
            self.display.backspace()
        elif text in ["MC", "MR", "M+", "M-"]:
            self.handle_memory(text)
        else:
            self.display.insert(text)

    def handle_engineering_input(self, text):
        if text == "Deg/Rad":
            self.angle_mode = 'deg' if self.angle_mode == 'rad' else 'rad'
            self.display.setText(f"Angle Mode: {self.angle_mode}")
        elif text in {"sin", "cos", "tan", "asin", "acos", "atan", "log", "ln", "sqrt", "!", "^", "π", "e"}:
            self.handle_advanced_function(text)
        else:
            self.handle_standard_input(text)

    def handle_advanced_function(self, func):
        try:
            if func == "π":
                self.display.insert(str(math.pi))
                return
            elif func == "e":
                self.display.insert(str(math.e))
                return
                
            value = float(self.display.text())
            if func in {"sin", "cos", "tan", "asin", "acos", "atan"}:
                if self.angle_mode == 'deg':
                    value = math.radians(value)
                result = getattr(math, func)(value)
                if func in {"asin", "acos", "atan"} and self.angle_mode == 'deg':
                    result = math.degrees(result)
            elif func == "log":
                result = math.log10(value)
            elif func == "ln":
                result = math.log(value)
            elif func == "sqrt":
                result = math.sqrt(value)
            elif func == "!":
                if value < 0 or not value.is_integer():
                    raise ValueError("Factorial requires non-negative integer.")
                result = math.factorial(int(value))
            else:
                return
                
            self.display.setText(str(result))
            self.log_history(f"{func}({value})", result)
        except Exception as e:
            self.show_error_message(str(e))

    def handle_memory(self, operation):
        try:
            current = float(self.display.text())
            if operation == "MC":
                self.memory = 0
            elif operation == "MR":
                self.display.setText(str(self.memory))
            elif operation == "M+":
                self.memory += current
            elif operation == "M-":
                self.memory -= current
        except:
            self.show_error_message("Invalid value for memory operation")

    def calculate_result(self):
        try:
            expr = self.display.text().replace("^", "**")
            result = simple_eval(
                expr,
                functions={
                    'sin': math.sin,
                    'cos': math.cos,
                    'tan': math.tan,
                    'asin': math.asin,
                    'acos': math.acos,
                    'atan': math.atan,
                    'log': math.log10,
                    'ln': math.log,
                    'sqrt': math.sqrt,
                    'factorial': math.factorial,
                },
                names={'pi': math.pi, 'e': math.e}
            )
            self.display.setText(str(result))
            self.log_history(expr, result)
        except (NameNotDefined, FunctionNotDefined, SyntaxError) as e:
            self.show_error_message(f"Error in expression: {e}")
        except ZeroDivisionError:
            self.show_error_message("Cannot divide by zero")
        except Exception as e:
            self.show_error_message(f"Calculation error: {str(e)}")

    def log_history(self, expr, result):
        entry = f"{QDateTime.currentDateTime().toString('hh:mm:ss')} {expr} = {result}"
        self.history.append(entry)
        self.history_panel.append(entry)

    def clear_history(self):
        self.history_panel.clear()
        self.history = []

    def show_error_message(self, msg):
        QMessageBox.critical(self, "Error", msg)
        self.display.setText("Error")

    def keyPressEvent(self, event: QKeyEvent):
        key = event.text()
        if key in "0123456789.+-*/()^":
            self.display.insert(key)
        elif event.key() in (Qt.Key_Enter, Qt.Key_Return):
            self.calculate_result()
        elif event.key() == Qt.Key_Backspace:
            self.display.backspace()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    calc = CalculatorApp()
    calc.show()
    sys.exit(app.exec_())