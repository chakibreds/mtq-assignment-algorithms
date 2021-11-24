from algorithme import *
import json, sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py <preferences.json>")
        exit(1)
    
    file_name = sys.argv[1]

    # load data
    with open(file_name) as file:
        data = json.load(file)

    filename = "output/result.csv"

    affectationStudents = []#galeShapleyStudents(data)
    affectationInstituts = galeShapleyInstituts(data)

    print("Affectation priorité aux étudiants :")
    writeAffectation(affectationInstituts, filename, format='csv')

    drawGraph(filename)

    print("\nPriorité aux étudiants : ")
    print(f"Satisfaction des étudiants : {studentSatisfaction(affectationStudents,data)}")
    print(f"Satisfaction des instituts : {institutionSatisfaction(affectationStudents,data)}")

    print("\nAffectation priorité aux institutions :")
    printAffectation(affectationInstituts)

    print("\nPriorité aux institutions : ")
    print(f"Satisfaction des étudiants : {studentSatisfaction(affectationInstituts,data)}")
    print(f"Satisfaction des instituts : {institutionSatisfaction(affectationInstituts,data)}")
