# Flask Excel Download App

This is a simple Flask application that converts CSV data to Excel format.
It has two endpoints: one for downloading the Excel file as a blob and another for saving the file to a folder with a download link.

## Features

- Convert CSV data to Excel.
- Two download options:
  - Download as a blob.
  - Save to file and provide a download URL.

## Prerequisites

Make sure you have Python installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

## Installation

1. Clone this repository:

   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

## Running the App

1. Run the Flask app:

   ```bash
   python app.py
   ```

2. Open your browser and go to `http://127.0.0.1:5000/`.

3. Click the buttons to download the Excel file.

## License

This project is licensed under the MIT License.
