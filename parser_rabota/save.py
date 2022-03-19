import csv


def save_to_csv(jobs):
    with open("test.csv", "w", encoding="utf8") as f:
        writer = csv.writer(f)
        writer.writerow(["company", "title", "link", "location"])
        for job in jobs:
            writer.writerow(list(job.values()))
    return


def save_dev_to_csv(jobs, name):
    with open(f"{name}.csv", "w", encoding="utf8") as f:
        writer = csv.writer(f)
        writer.writerow(["title", "company", "link", "salary"])
        for job in jobs:
            writer.writerow(list(job.values()))
    return
