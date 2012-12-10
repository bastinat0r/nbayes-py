from functools import *

def read_data(file_name):
    data = []
    with open(file_name, "r") as f:
        data = f.read().split("\n")
    data = [tuple(s.split(",")) for s in data if len(s) > 0]
    return data

def paivj(data, instance, c):
    p = 1
    for i in range(len(data[0])-1):
        l = [d[-1] for d in data if d[i] == instance[i]]
        p *= l.count(c) * 1.0 / len(l)
    return p

def classify(instance, data):
    classes = set([t[-1] for t in data])
    classes = [(t, [f[-1] for f in data].count(t)) for t in classes]
    print(classes)
    plist = [(c[0],
            paivj(data,instance, c[0]) * c[1] * 1.0 / reduce(lambda x,y : x[1] + y[1], classes)
    ) for c in classes];
    print(plist);

if __name__ == "__main__":
    data = read_data("tennis.csv")
    print(data)
    classify(data[0], data)
