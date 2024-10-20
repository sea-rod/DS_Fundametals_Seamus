def open_file(path):
    with open(path, "r") as file:
        review_data = []
        review = file.readline().strip("\n").split("\t").index("Review")
        for i in file.readlines():
            review_data.append(i.strip("\n").split("\t")[review])
    return review_data


def write_file(path, data):
    with open(path, "w") as file:
        for i in data:
            file.write(i + "\n")
