from pprint import pprint
import sys

def print_sum(file_name: str):
    with open(file_name) as f:
        headers = f.readline().strip().split(",")
        lines = f.readlines()

    score = {v: 0 for v in headers}
    for line in lines:
        for i, v in enumerate(line.split(",")):
            score[headers[i]] += int(v)
    del score["hole"]
    pprint(score)


if __name__ == "__main__":
        
    fn = sys.argv[1] if len(sys.argv) > 1 else "golf.txt"
    print_sum(fn)
