import requests
import base64


def get_repos(org_name, headers):
    url = f"https://api.github.com/orgs/{org_name}/repos?per_page=100"
    repos = []
    while url:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            repos.extend(response.json())
            # Check if there is a next page
            if 'next' in response.links:
                url = response.links['next']['url']
            else:
                url = None
        else:
            print(f"Failed to fetch repositories: {response.status_code}")
            break
    return repos


def get_readme(repo, headers):
    readme_url = repo['url'] + "/readme"
    response = requests.get(readme_url, headers=headers)
    if response.status_code == 200:
        readme_content = response.json().get('content', '')
        readme_html_url = response.json().get('html_url', '')
        return base64.b64decode(readme_content).decode('utf-8'), readme_html_url
    else:
        print(f"Failed to fetch README for {repo['name']}: {response.status_code}")
        return None, None


def main(org_name, keyword, token):
    headers = {
        "Authorization": f"token {token}"
    }
    repos = get_repos(org_name, headers)
    scanned_count = 0
    keyword_count = 0
    keyword_repos = []

    for repo in repos:
        readme_content, readme_url = get_readme(repo, headers)
        scanned_count += 1
        print(f"README URL: {readme_url if readme_url else 'Not Found'}")
        if readme_content and keyword in readme_content:
            keyword_count += 1
            keyword_repos.append(repo['name'])
            print(f"Repository: {repo['name']} contains {keyword} in its README.md")
        print("=" * 80)

    print(f"Total scanned repositories: {scanned_count}")
    print(f"Total repositories containing '{keyword}': {keyword_count}")
    if keyword_count > 0:
        print("Repositories containing the keyword:")
        for repo in keyword_repos:
            print(f"- {repo}")
    else:
        print("Repositories containing the keyword: 0")


if __name__ == "__main__":
    # Replace here with the organization name and keywords you need to scan, as well as your GitHub token.
    org_name = "CasbinRuby"  # Please fill in the name of the organization you need to scan here.
    keyword = "[![Gitter]"  # Please enter the keywords you are looking for here.
    token = "ghp_**********"  # Please fill in your GitHub token here.
    main(org_name, keyword, token)
