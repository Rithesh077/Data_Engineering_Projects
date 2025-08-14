# GitHub Trending Python Repositories - ETL Pipeline

## Project Overview

This project is a foundational data engineering task that builds a complete, end-to-end ETL (Extract, Transform, Load) pipeline.

The pipeline performs the following steps:

1.  **Extract:** Fetches data about the most popular Python repositories from the live GitHub API.
2.  **Transform:** Cleans and structures the raw JSON data, extracting only the most relevant fields.
3.  **Load:** Saves the clean, processed data into a structured CSV file for easy analysis.

This project serves as a practical demonstration of core data engineering skills, including API consumption, data processing, and data storage.

## Tech Stack

- **Language:** Python
- **Core Libraries:**
  - `requests`: For making HTTP requests to the GitHub API.
  - `pandas`: For data transformation and for loading the data into a CSV file.

## How to Run

1.  **Clone the repository:**
    ```bash
    git clone
    ```
2.  **Navigate to the project directory:**
    ```bash
    cd [repository-folder-name]
    ```
3.  **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Run the pipeline:**
    ```bash
    python project1.py
    ```

The output will be a file named `repo_data.csv` in the same directory, containing the latest trending repository data.

## Next Steps

The next phase of this project will involve:

- Loading the data into a structured database (SQLite).
- Automating the pipeline to run on a daily schedule.
