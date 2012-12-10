

def read_data(file_name):
    data = []
    with open(file_name, "r") as f:
        data = f.read().split("\n")
    data = [tuple(s.split(",")) for s in data if len(s) > 0]
    return data


if __name__ == "__main__":
    data = read_data("tennis.csv")
    print data
