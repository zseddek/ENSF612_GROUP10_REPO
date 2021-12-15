from github import Github
api = Github("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")

def pull_from_api(repository_name):
    repo = api.get_repo(repository_name)
    file_content = repo.get_contents('README.md')
    string_readme_mchn = file_content.decoded_content
    encoding = 'utf-8'
    string_readme  = str(string_readme_mchn, encoding)
    repository_name = repository_name.replace("/","_")
    f = open("new_records//" + repository_name + ".md", "w")
    f.write(string_readme)
    f.close()

def main():

    success = 0
    with open("repo_links.txt", "r") as fd:
        for line in fd:
            if (success > 1499):
                print("1500 README.md files have been succesfully collected")
                break
            line = line.strip()
            if (line != "null"):
                try:
                    pull_from_api(line[19:])
                    success += 1
                    print("README.md file found!")
                except:
                    print("Repo has been deleted or no README.md available")
            else:
                continue

    print(success, "README.md files have been aquired")

 
if __name__ == "__main__":
    main()