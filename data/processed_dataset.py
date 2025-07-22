import json
from datasets import Dataset

def load_dataset():
    with open("data/raw_data.json", "r") as f:
        data = json.load(f)
    return Dataset.from_list(data)

if __name__ == "__main__":
    ds = load_dataset()
    print(ds)
