import json

# Function to get repo and repo type
def get_repos_by_type(type):
    results = []
    for repo in data_json["result"]:
        if repo["type"] == type:
         results.append(repo)
    return results

def count_files_and_size_in_repos(repos):
    num_files = 0
    size = 0
    for repo in repos:
        for file in repo["files"]:
            num_files += 1
            size += file["file_size"]
    return {
        "number_of_files": num_files,
        "size_of_files": size
    }

if __name__ == '__main__':
    f = open("./artifactory.json")
    data_json = json.load(f)



    # print(get_repos_by_type("npm"))
    # filtered_repos = get_repos_by_type("npm")
    # print(count_files_and_size_in_repos(filtered_repos))


