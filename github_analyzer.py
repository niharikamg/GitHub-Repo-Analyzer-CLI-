import argparse
import requests
import pandas as pd

GITHUB_API_URL = "https://api.github.com/repos/{}/{}"

def fetch_repo_data(owner, repo):
    url = GITHUB_API_URL.format(owner, repo)
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return {
            "Repository": repo,
            "Owner": owner,
            "Stars": data.get("stargazers_count", 0),
            "Forks": data.get("forks_count", 0),
            "Open Issues": data.get("open_issues_count", 0),
            "Watchers": data.get("watchers_count", 0),
            "Default Branch": data.get("default_branch", "N/A"),
            "Last Updated": data.get("updated_at", "N/A"),
        }
    else:
        print(f"❌ Failed to fetch data for {owner}/{repo}")
        return None

def main(repos, output_file):
    repo_data = []
    
    for repo in repos:
        try:
            owner, repo_name = repo.split('/')
            data = fetch_repo_data(owner, repo_name)
            if data:
                repo_data.append(data)
        except ValueError:
            print(f"⚠️ Invalid format for repo '{repo}'. Use 'owner/repo' format.")
    
    if repo_data:
        df = pd.DataFrame(repo_data)
        if output_file.endswith(".csv"):
            df.to_csv(output_file, index=False)
        else:
            df.to_json(output_file, indent=4)
        
        print(f"✅ Repository data saved to '{output_file}'")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="GitHub Repo Analyzer - Fetches repo statistics.")
    parser.add_argument("repos", nargs="+", help="List of GitHub repositories in 'owner/repo' format.")
    parser.add_argument("-o", "--output", default="repo_stats.json", help="Output file (CSV or JSON).")

    args = parser.parse_args()
    main(args.repos, args.output)
