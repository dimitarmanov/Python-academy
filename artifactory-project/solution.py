import json

from datetime import datetime
from sqlite3 import Date


def get_repos_by_type(type):
    results = []

    for repo in data_json["result"]:
        if repo["type"] == type:
            results.append(repo)

    return results


def count_files_and_size_in_repos(repos, file_types, start_date, end_date):
    files = 0
    size = 0

    for repo in repos:
        for file in repo["files"]:
            date = datetime.strptime(file['file_date'], "%Y-%m-%d").date()
            if file["file_type"] == file_types and start_date < date < end_date:
                files += 1
                size += file["file_size"]

                print(date.today() - date)

    return {
        "number_of_files": files,
        "size_of_files": size
    }


if __name__ == '__main__':
    f = open("./artifactory.json")
    data_json = json.load(f)

    filtered_repos = get_repos_by_type("npm")
    count_files_and_sizes = count_files_and_size_in_repos(filtered_repos, "jpg", Date(1999,2,3), Date(2002,2,3))
    print(count_files_and_sizes)
