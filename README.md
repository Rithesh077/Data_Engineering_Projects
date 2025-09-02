# GitHub Trending Python Repositories - ETL Pipeline

## Project Overviw

This project is a dynamic, interactive ETL (Extract, Transform, Load) pipeline.

Instead of a static script, this tool prompts the user for a search topic (e.g., "machine learning") and a list of specific data fields (e.g., `name`, `owner`, `stars`). It then performs the following steps:

1.  **Extract:** Dynamically builds a query and fetches the relevant data from the live GitHub API.
2.  **Transform:** Cleans and structures the raw JSON response, extracting only the fields the user requested.
3.  **Load:** Displays the final, processed data in a clean, tabular format directly in the console.

This project serves as a practical demonstration of core data engineering skills, including API consumption, data processing, and data storage.

## Tech Stack

- **Language:** Python
- **Core Libraries:**
  - `requests`: For making HTTP requests to the GitHub API.
  - `pandas`: For data transformation and for loading the data into a CSV file.

## How to Run

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/Rithesh077/Data_Engineering_Projects.git
    ```
2.  **Navigate to the project directory and set up the environment:**
    ```bash
    cd Data_Engineering_Projects
    python -m venv .venv
    .\.venv\Scripts\Activate.ps1
    ```
3.  **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Run the pipeline:**
    ```bash
    python Github_repo_pipeline.py
    ```
5.  **Follow the prompts:** The script will ask you to enter a search topic and a comma-separated list of fields to display. For example:
    - **Topic:** `pandas`
    - **Fields:** `name,stars,owner,description`

## Next Steps

The next phase of this project will involve:

- Loading the data into a structured database (SQLite).
- Automating the pipeline to run on a daily schedule.
