# GitHub Repo Analyzer

## 📌 Description
The **GitHub Repo Analyzer** is a command-line tool that fetches and analyzes GitHub repository data such as stars, forks, issues, and contributors.

## 🚀 Features
- Fetch repository details (stars, forks, issues, watchers, last updated, etc.).
- Analyze multiple repositories at once.
- Save data in **CSV or JSON** format.
- Simple command-line interface.

## 🛠 Requirements
Ensure you have **Python 3.6+** installed. Install dependencies with:
```sh
pip install requests pandas
```

## 📄 Usage
Run the script with the following command:
```sh
python github_analyzer.py user/repo -o repo_stats.json
```
or for multiple repositories:
```sh
python github_analyzer.py user/repo1 user/repo2 -o repos.csv
```

## 📜 License
This project is open-source and available under the MIT License.

