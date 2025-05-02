import requests

GITHUB_USERNAME = "alishazin"
GITHUB_TOKEN = open("token.txt").read()

headers = {
    "Authorization": f"token {GITHUB_TOKEN}"
}

def get_repos(username):
    repos = []
    page = 1
    while True:
        url = f"https://api.github.com/users/{username}/repos?per_page=30&page={page}"
        res = requests.get(url, headers=headers)
        data = res.json()
        if not data:
            break
        repos.extend(data)
        page += 1
    return repos

def get_contributors(repo_full_name):
    url = f"https://api.github.com/repos/{repo_full_name}/contributors"
    res = requests.get(url, headers=headers)
    return len(res.json())

def main():
    repos = get_repos(GITHUB_USERNAME)
    if not repos:
        print("No repositories found.")
        return

    print(f"\n📊 Repo analysis for GitHub user: {GITHUB_USERNAME}")
    total_stars = 0
    results = []

    for repo in repos:
        name = repo["name"]
        full_name = repo["full_name"]
        stars = repo["stargazers_count"]
        contributors = get_contributors(full_name)

        total_stars += stars
        results.append({
            "name": name,
            "stars": stars,
            "contributors": contributors,
        })

    results.sort(key=lambda x: x["stars"], reverse=True)

    print(f"\n⭐ Total Stars: {total_stars}")
    print(f"\n🔍 Top 10 Repositories (By Stars):")
    for repo in results[:10]:
        print(f"{repo['name']}: {repo['stars']} ⭐ | {repo['contributors']} contributors")

if __name__ == "__main__":
    main()
