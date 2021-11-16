from algorithme import galeShapley, printAffectation, satisfaction
import json, sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py <preferences.json>")
        exit(1)
    
    file_name = sys.argv[1]

    # load data
    with open(file_name) as file:
        data = json.load(file)

    affectation = galeShapley(data)

    print("Institutions : [Étudiants affectés]")
    printAffectation(affectation)

    print(f"Satisfaction des étudiants : {satisfaction(affectation,data)}")