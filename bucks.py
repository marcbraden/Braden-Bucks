import json
def print_json(name):
    print(json.dumps(json.load(open(name,'r'))))
print_json("ledger.json")
