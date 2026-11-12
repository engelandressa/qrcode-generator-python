# QR Code Generator (Python)
[![Ask DeepWiki](https://devin.ai/assets/askdeepwiki.png)](https://deepwiki.com/engelandressa/qrcode-generator-python)

This repository contains a collection of Python scripts for generating various types of QR codes. It includes both simple command-line tools and more advanced graphical user interfaces (GUIs) built with Tkinter.

## Features

*   **Multiple Data Types**: Generate QR codes for URLs, plain text, phone numbers, email addresses, and Wi-Fi network credentials.
*   **Interface Options**: Choose between a minimal command-line script or two different GUI applications.
*   **Easy to Use**: Simple and straightforward scripts that are easy to run.
*   **Image Output**: Saves the generated QR code as a `.png` file.

## Scripts Overview

This project includes three different scripts for generating QR codes:

1.  `qrcode-generator-python.py`: The most advanced script, featuring a GUI that allows you to select the type of QR code to generate (Link, Text, Phone, E-mail, or Wi-Fi). The interface updates dynamically based on your selection.

2.  `qrcode-generator-link-python.py`: A simple GUI application specifically for generating a QR code from a web link.

3.  `qrcode-generator-link-simple.py`: A basic command-line script that prompts the user for a URL in the terminal and generates a QR code.

## Requirements

*   Python 3
*   `qrcode` library

## Installation

1.  Clone the repository to your local machine:
    ```bash
    git clone https://github.com/engelandressa/qrcode-generator-python.git
    ```

2.  Navigate into the project directory:
    ```bash
    cd qrcode-generator-python
    ```

3.  Install the required Python package:
    ```bash
    pip install qrcode[pil]
    ```

## Usage

You can run any of the three scripts depending on your needs.

### Advanced GUI Version

This version provides the most functionality.

1.  Run the script from your terminal:
    ```bash
    python qrcode-generator-python.py
    ```
2.  In the application window, select the type of QR code you want to create from the dropdown menu.
3.  Enter the required information (e.g., link, Wi-Fi name and password).
4.  Click the "Gerar QR Code" button.
5.  The QR code will be saved as `meu_qrcode.png` in the project directory.

### Simple GUI Version (Link only)

Use this for quickly creating a QR code from a URL.

1.  Run the script:
    ```bash
    python qrcode-generator-link-python.py
    ```
2.  Enter the link into the input field.
3.  Click the "Gerar QR Code" button.
4.  The QR code will be saved as `meu_qrcode.png`.

### Command-Line Version (Link only)

The simplest way to generate a QR code from a URL.

1.  Run the script:
    ```bash
    python qrcode-generator-link-simple.py
    ```
2.  When prompted in the terminal, paste your URL and press Enter.
3.  The QR code will be saved as `qrcode.png`.
