import requests
import json
from github import Github
api = Github("GITHUB ACCESS TOKEN")
api = Github("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")

def get_repo_links():
    since = 20000
    public_urls = []
    while (since < 25000):
        request_link = "https://api.github.com/repositories?since=" + str(since)
        response = requests.get(request_link)
        get_result = json.loads(response.text)
        for i in range(len(get_result)):
            public_urls.append(str(get_result[i]["html_url"]))
        since += 100
    return public_urls  # List of public URLs


def pull_from_api(repository_name):
    repo = api.get_repo(repository_name)
    file_content = repo.get_contents('README.md')
    string_readme_mchn = file_content.decoded_content
    encoding = 'utf-8'
    string_readme = str(string_readme_mchn, encoding)
    repository_name = repository_name.replace("/", "_")
    f = open("new_records//" + repository_name + ".md", "w")
    f.write(string_readme)
    f.close()


def main():
    success = 0
    public_repo_links = get_repo_links()
    for line in public_repo_links:
        try:
            pull_from_api(line[19:])
            success += 1
            print("README.md file found!")
        except:
            print("Error occurred while attempting to pull README.md")

    print(success, "README.md files have been aquired")


if __name__ == "__main__":
    main()
