# project1_final.py

import sqlite3
import requests


def fetch_and_process_github_repos():
    """
    Fetches trending Python repositories from the GitHub API,
    processes the data, and saves it to a CSV file.
    """
    # E: Extract
    url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        repo_list = data['items']
    except requests.exceptions.RequestException as e:
        print(f"Error during API request: {e}")
        return
    except KeyError:
        print("Error: 'items' key not found in the response.")
        return

    # T: Transform
    cleaned_data = []
    for repo in repo_list:
        processed_repo = {
            'name': repo.get('name'),
            'owner': repo.get('owner', {}).get('login'),
            'stars': repo.get('stargazers_count'),
            'url': repo.get('html_url'),
            'description': repo.get('description')
        }
        cleaned_data.append(processed_repo)

    # L: Load
    print("Connecting to database and loading data...")
    connection = None
    try:
        connection = sqlite3.connect("trending_repos.db")
        cursor = connection.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS repos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            owner TEXT,
            stars INTEGER,
            url TEXT UNIQUE,
            description TEXT,
            fetched_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
        for repo in cleaned_data:  # type: ignore
            try:
                cursor.execute("""
                INSERT OR IGNORE INTO repos (name, owner, stars, url, description)
                VALUES (?, ?, ?, ?, ?)
                """, (repo['name'], repo['owner'], repo['stars'], repo['url'], repo['description']))
            except sqlite3.Error as e:
                print(
                    f"Could not insert data for repo {repo.get('name')}: {e}")
        connection.commit()
        print("Data successfully loaded into the database.")

    except sqlite3.Error as e:
        print(f"Database error: {e}")

    finally:
        if connection:
            connection.close()
    print("Trending Python Repositories:\n")


if __name__ == "__main__":
    fetch_and_process_github_repos()
