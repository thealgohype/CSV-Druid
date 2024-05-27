# CSV Druid: The Ultimate CSV Analyzer
![CSV-Druid : Analysis and Insights from Data](https://github.com/thealgohype/CSV-Druid/blob/main/images/csv-druid-gitpage.png)

Want to see CSV-Druid in action? [Click HERE](https://csv-analyzer.replit.app).

Welcome to **CSV Druid**, a powerful and user-friendly CSV analyzer that leverages the capabilities of PandasAI for comprehensive data analysis. This application is built using Streamlit for an intuitive and interactive user interface.

## Table of Contents
1. [Introduction](#introduction)
2. [Features](#features)
3. [Installation](#installation)
4. [Usage](#usage)
5. [How It Works](#how-it-works)
6. [Contributing](#contributing)
7. [License](#license)

## Introduction
CSV Druid is designed to help you effortlessly analyze your CSV files. By uploading your CSV data, you can quickly gain insights through data analysis suggestions, visualizations, and summaries. The combination of Streamlit and PandasAI makes this tool both powerful and easy to use.

## Features
- **Upload CSV Files**: Easily upload your CSV files through a user-friendly interface.
- **Data Analysis**: Get automatic data analysis suggestions powered by PandasAI.
- **Visualizations**: Generate and customize various plots and graphs.
- **Summary Statistics**: View essential summary statistics for your data.
- **Interactive Interface**: Enjoy a smooth and interactive experience with Streamlit.
- **Model Selection**: Choose from a variety of models including GPT-3.5, GPT-4, Claude, and Google Gemini for analysis.

## Installation

### Prerequisites
Ensure you have the following installed on your system:
- Python 3.7 or higher
- pip (Python package installer)

### Steps
1. **Clone the repository:**
   ```sh
   git clone https://github.com/thealgohype/CSV-Druid.git
   cd CSV-Druid
   ```

2. **Create and activate a virtual environment (optional but recommended):**
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install the required dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

## Usage
1. **Run the application:**
   ```sh
   streamlit run main.py
   ```

2. **Open your web browser:**
   The Streamlit app will automatically open in your default web browser. If it doesn't, navigate to `http://localhost:8501` in your browser.

3. **Upload your CSV file:**
   Use the file uploader in the sidebar to upload your CSV file.

4. **Analyze your data:**
   Once uploaded, CSV Druid will automatically analyze your data and provide insights, visualizations, and summary statistics.

## How It Works
CSV Druid is built using the following key components:
- **Streamlit**: Provides a smooth and interactive user interface.
- **PandasAI**: Powers the data analysis engine to deliver insights and visualizations.
- **Language Models**: Allows the selection of different language models for analysis, including GPT-3.5, GPT-4, Claude, and Google Gemini.

### Main Components
- `main.py`: The entry point of the application. It handles the user interface and interactions contains the main engine for the web-app.


### Example Usage
Here is a simple example of how to use CSV Druid:
1. Start the application by running `streamlit run main.py`.
2. Upload a CSV file through the File Uploader widget at the top.
3. Enter your analysis question in the text input field.
4. View the automatically generated data analysis, visualizations, and summary statistics.

### Code Reference
The core functionality of CSV Druid is implemented in `main.py` as follows:


## Contributing
We welcome contributions from the community! Here’s how you can help:
1. **Fork the repository** on GitHub.
2. **Clone your fork** to your local machine:
   ```sh
   git clone https://github.com/thealgohype/CSV-Druid.git
   ```
3. **Create a new branch** for your feature or bugfix:
   ```sh
   git checkout -b feature-name
   ```
4. **Commit your changes** and **push** your branch to GitHub:
   ```sh
   git add .
   git commit -m "Add feature"
   git push origin feature-name
   ```
5. **Open a pull request** on GitHub, and we’ll review your changes.

## License
This project is licensed under the MIT License.

---


We hope you find CSV Druid useful for your data analysis needs. If you have any questions or feedback, feel free to open an issue on GitHub or contact us directly. Happy analyzing!