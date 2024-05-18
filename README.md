# readme-checker

This script scans all repositories in a specified GitHub organization for a specific keyword in their README files. It uses the GitHub API to fetch repository information and README content.

## Requirements

- Python 3.x
- `requests` library

You can install the `requests` library using pip:

```bash
pip install requests
```

## Usage

### 1. Clone the Repository

First, clone the repository to your local machine:

```bash
git clone <repository-url>
```

### 2. Set Up Your Environment

Before running the script, you need to set up your environment by providing the required parameters:

- **Organization Name**: The name of the GitHub organization you want to scan.
- **Keyword**: The keyword you want to search for in the README files.
- **GitHub Token**: Your GitHub API token for authentication.

### 3. Run the Script

Open the **`main.py`** file and replace the placeholder values with your actual data:

```python
if __name__ == "__main__":
    # Replace here with the organization name and keywords you need to scan, as well as your GitHub token.
    org_name = "jcasbin"  # Please fill in the name of the organization you need to scan here.
    keyword = "[![Gitter]"  # Please enter the keywords you are looking for here.
    token = "ghp_**********"  # Please fill in your GitHub token here.
    main(org_name, keyword, token)
```

### 4. Execute the Script

Run the script using Python:

```bash
python main.py
```

## Script Description

### `get_repos(org_name, headers)`

Fetches all repositories of a given organization.

- **`org_name`**: The name of the organization.
- **`headers`**: Headers for the HTTP request, including the authorization token.

### `get_readme(repo, headers)`

Fetches the README file content for a given repository.

- **`repo`**: The repository object.
- **`headers`**: Headers for the HTTP request, including the authorization token.

### `main(org_name, keyword, token)`

Main function to scan all repositories and search for the keyword in their README files.

- **`org_name`**: The name of the organization.
- **`keyword`**: The keyword to search for in the README files.
- **`token`**: Your GitHub API token for authentication.

### Output

The script will output the following information:

1. The URL of each README file (or "Not Found" if the README does not exist).
2. The name of the repository if the keyword is found in its README file.
3. The total number of scanned repositories.
4. The total number of repositories containing the keyword.
5. A list of repositories containing the keyword (if any).

## Example Output

```markdown
README URL: https://github.com/jcasbin/example-repo/blob/main/README.md
Repository: example-repo contains [![Gitter] in its README.md
================================================================================
Total scanned repositories: 10
Total repositories containing '[![Gitter]': 2
Repositories containing the keyword:

- example-repo1
- example-repo2
```

## **Notes**

- Ensure your GitHub token has the necessary permissions to access the repositories of the specified organization.
- The **`per_page=100`** parameter is used to fetch up to 100 repositories per API call. If the organization has more than 100 repositories, the script will handle pagination automatically.
