
# QR Code Generator

A simple Flask web application to generate and download QR codes.

## Overview

This web application allows users to input data, generate a QR code, and download the QR code image. The generated QR codes have an expiration time, and the application supports customization of the QR code file name.

## Features

- Input data to be encoded into a QR code.
- Customize the QR code file name.
- Generate and download QR codes.
- QR codes have an expiration time.

## Getting Started

### Prerequisites

- Python 3.x
- Flask

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/DevClube/qrcodegenerator.git
   cd qrcodegenerator
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:

   ```bash
   python app.py
   ```

4. Open your web browser and go to [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

## Usage

1. Enter the data you want to encode into the QR code.
2. Optionally, customize the QR code file name.
3. Click the "Generate QR Code" button.
4. The generated QR code will be displayed, and you can download it using the provided button.

## Customization

- Adjust the expiration time for QR codes in the `generate_qr` route.
- Modify the HTML and CSS files in the `templates` folder for additional styling.


## Acknowledgments

- This project uses the [Flask](https://flask.palletsprojects.com/) web framework.
- QR code generation is powered by the [qrcode](https://pypi.org/project/qrcode/) library.
