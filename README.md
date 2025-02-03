# SciCalcPro - Advanced Calculator

SciCalcPro is an advanced scientific calculator application built using Python and PyQt5. It supports standard and engineering modes, history tracking, and customizable themes.

## Features
- **Standard Mode:** Basic arithmetic operations.
- **Engineering Mode:** Advanced functions like trigonometry, logarithms, factorial, and power calculations.
- **Memory Functions:** Store and retrieve values with `MC`, `MR`, `M+`, and `M-`.
- **History Panel:** View previous calculations.
- **Theme Support:** Light and dark mode.
- **Standalone Executable:** The project includes a compiled `.exe` file for Windows users.

## Installation
### Requirements
- Python 3.x
- PyQt5
- simpleeval

### Install Dependencies
```sh
pip install PyQt5 simpleeval
```

## Files Overview

### Application Files
- **SciCalcPro.py**: Main application script implementing the UI and calculator logic.
  - Uses **PyQt5** for GUI elements.
  - Implements **QMainWindow** for structuring the main application window.
  - Features a **QTabWidget** with both Standard and Engineering modes.
  - Supports **QPushButton** for calculator keys and operations.
  - Handles **QLineEdit** for input display and calculation processing.
  - Includes a history panel using **QTextEdit** to track previous calculations.
  - Implements **themes** (light and dark) via PyQt5 styling.
  - Supports **keyboard input** and shortcuts for a better user experience.
  - Uses **simpleeval** to safely evaluate mathematical expressions.

- **calculator.exe**: Precompiled executable version of the application containing all necessary dependencies.

### Internal Dependencies
- **PyQt5/**: Folder containing PyQt5 dependencies.
- **_.bz2.pyd, _decimal.pyd, _hashlib.pyd, _lzm.pyd, _socket.pyd, select.pyd, unicodedata.pyd**: Python extension modules required by the application.
- **base_library.zip**: Contains standard Python libraries packaged for the application.
- **libcrypto-3.dll**: Cryptographic library required for security features.
- **python3.dll, python313.dll**: Required Python runtime dynamic-link libraries.
- **VCRUNTIME140.dll, VCRUNTIME140_1.dll**: Visual C++ runtime libraries needed for execution.

### Assets
- **image.png**: Example image or application screenshot.

## Usage
Run the Python script:
```sh
python SciCalcPro.py
```
Or use the executable:
```sh
./calculator.exe
```

## Code Overview
The `SciCalcPro.py` script consists of the following main components:
- **`CalculatorApp(QMainWindow)`**: The main class responsible for handling the application.
- **`init_ui()`**: Initializes the UI components, including the display, buttons, and tabs.
- **`create_menu()`**: Generates the menu bar for theme selection and history management.
- **`init_standard_mode()` & `init_engineering_mode()`**: Define button layouts and functionalities for different calculator modes.
- **`handle_standard_input()` & `handle_engineering_input()`**: Process user input and execute mathematical functions.
- **`calculate_result()`**: Evaluates mathematical expressions and updates the display.
- **`log_history()`**: Stores and displays previous calculations.
- **`set_light_theme()` & `set_dark_theme()`**: Apply different UI themes.
- **`keyPressEvent(QKeyEvent)`**: Enables keyboard interaction for seamless usability.

## License
This project is licensed under the MIT License.

## Author
GitHub: [shxel](https://github.com/shxel)

