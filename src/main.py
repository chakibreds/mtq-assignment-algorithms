from algorithme import *
import json, sys, time

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python main.py <preferences.json> <output/dir/>")
        exit(1)
    
    file_name = sys.argv[1]
    output_dir = sys.argv[2]
    if output_dir[-1] != '/':
        output_dir += '/'

    # load data
    with open(file_name) as file:
        data = json.load(file)

    start = time.time()
    affectationStudents = galeShapleyStudents(data)
    end = time.time()
    affectationInstituts = galeShapleyInstituts(data)
    end_two = time.time()

    print(f"Temps d'execution Gale Shapley - priorité aux étudiants: {round(end - start,3)} secondes.")
    print(f"Temps d'execution Gale Shapley - priorité aux instituts: {round(end_two - end, 3)} secondes.")

    filename = output_dir + file_name.split('/')[-1].split('.')[0] + "_student" + ".json"
    writeAffectation(affectationStudents, filename, format=filename.split('.')[-1])
    filename = output_dir + file_name.split('/')[-1].split('.')[0] + "_institut" + ".json"
    writeAffectation(affectationInstituts, filename, format=filename.split('.')[-1])

    print("\nPriorité aux étudiants : ")
    for fonction in ['linear', 'poly', 'inverse']:
        print(f"\tSatisfaction '{fonction}' des étudiants : {studentSatisfaction(affectationStudents,data,fonction)}")
    print(f"\tSatisfaction des instituts : {institutionSatisfaction(affectationStudents,data)}")

    print("\nPriorité aux institutions : ")
    for fonction in ['linear', 'poly', 'inverse']:
        print(f"\tSatisfaction '{fonction}' des étudiants : {studentSatisfaction(affectationInstituts,data,fonction)}")
    print(f"\tSatisfaction des instituts : {institutionSatisfaction(affectationInstituts,data)}")
