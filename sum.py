from pprint import pprint


def print_sum():
    with open("golf.txt") as f:
        headers = f.readline().strip().split(",")
        lines = f.readlines()

    score = {v: 0 for v in headers}
    for line in lines:
        for i, v in enumerate(line.split(",")):
            score[headers[i]] += int(v)
    del score["hole"]
    pprint(score)


if __name__ == "__main__":
    print_sum()
