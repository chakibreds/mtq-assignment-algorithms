from algorithme import GaleShapley
import json

if __name__ == "__main__":
    file_name = 'data/medium_preferences.json'

    with open(file_name) as file:
        data = json.load(file)

    #print(data)
    gs = GaleShapley(data)
    print(gs)
