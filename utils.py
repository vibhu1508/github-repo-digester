import requests
import base64

def fetch_repo_files(owner, repo, path=""):
    url = f"https://api.github.com/repos/{owner}/{repo}/contents/{path}"
    res = requests.get(url)
    res.raise_for_status()
    files = res.json()

    all_files = []
    for file in files:
        if file["type"] == "file":
            if file["name"].endswith((".py", ".js", ".ts", ".java", ".cpp")):
                content = requests.get(file["url"]).json()["content"]
                decoded = base64.b64decode(content).decode("utf-8", errors="ignore")
                all_files.append((file["path"], decoded))
        elif file["type"] == "dir":
            all_files += fetch_repo_files(owner, repo, file["path"])
    return all_files