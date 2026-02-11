import json
def print_json(name):
    print(json.dumps(json.load(open(name,'r'))))

transaction="from:Braden
